#!/usr/bin/env python3
"""OpenRouter JSON adapter for Gauntlet grading, planning, and appeals."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any

MODEL = "z-ai/glm-5.2"
ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"


class AdapterError(RuntimeError):
    pass


SCHEMAS: dict[str, dict[str, Any]] = {
    "grade-day": {
        "type": "object",
        "additionalProperties": False,
        "required": ["delivery_score", "mastery_score", "confidence", "summary", "evidence_citations"],
        "properties": {
            "delivery_score": {"type": "number", "minimum": 0, "maximum": 4, "multipleOf": 0.5},
            "mastery_score": {"type": "number", "minimum": 0, "maximum": 4, "multipleOf": 0.5},
            "confidence": {"enum": ["low", "medium", "high"]},
            "summary": {"type": "string"},
            "evidence_citations": {"type": "array", "items": {"type": "string"}},
        },
    },
    "plan-day": {
        "type": "object",
        "additionalProperties": False,
        "required": ["plan_markdown"],
        "properties": {
            "plan_markdown": {
                "type": "string",
                "minLength": 120,
                "maxLength": 8000,
                "pattern": "^# Daily Plan[^\\n]*\\n[\\s\\S]*## Required boundary[\\s\\S]*## Proof required[\\s\\S]*## Scope guard",
            }
        },
    },
    "appeal": {
        "type": "object",
        "additionalProperties": False,
        "required": ["decision", "rationale", "corrected_delivery_score", "corrected_mastery_score"],
        "properties": {
            "decision": {"enum": ["upheld", "denied", "review-needed"]},
            "rationale": {"type": "string"},
            "corrected_delivery_score": {"type": ["number", "null"], "minimum": 0, "maximum": 4, "multipleOf": 0.5},
            "corrected_mastery_score": {"type": ["number", "null"], "minimum": 0, "maximum": 4, "multipleOf": 0.5},
        },
    },
}


SYSTEM = {
    "grade-day": "Apply only the supplied rubric to the frozen evidence. Separate deterministic delivery facts from mastery judgment. Never award credit for missing evidence.",
    "plan-day": (
        "Create the next frozen daily boundary. Keep required work within the supplied run scope; "
        "prioritize critical-path defects before optional backlog work. Return concise Markdown only "
        "in plan_markdown, beginning with '# Daily Plan — YYYY-MM-DD' and containing, in order, "
        "'## Required boundary', '## Proof required', and '## Scope guard'. Put concrete bullet items "
        "under every section. Include no preamble, metadata dump, or instruction to ignore text."
    ),
    "appeal": "Judge only the disputed claim against the original frozen evidence and rubric. New evidence is inadmissible.",
}


def operation_for(request: dict[str, Any]) -> str:
    operation = request.get("operation")
    if operation == "appeal-grade":
        return "appeal"
    if operation not in SCHEMAS:
        raise AdapterError(f"unsupported operation: {operation}")
    return str(operation)


def call_openrouter(request: dict[str, Any], timeout: float = 120) -> dict[str, Any]:
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise AdapterError("OPENROUTER_API_KEY is not set")
    operation = operation_for(request)
    body = {
        "model": MODEL,
        "temperature": 0,
        "stream": False,
        "messages": [
            {"role": "system", "content": SYSTEM[operation]},
            {"role": "user", "content": json.dumps(request, separators=(",", ":"))},
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {"name": f"gauntlet_{operation.replace('-', '_')}", "strict": True, "schema": SCHEMAS[operation]},
        },
    }
    http_request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "X-OpenRouter-Title": "Gauntlet Controller",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(http_request, timeout=timeout) as response:
            provider = json.load(response)
    except urllib.error.HTTPError as exc:
        detail = exc.read(512).decode(errors="replace")
        raise AdapterError(f"OpenRouter HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        raise AdapterError(f"OpenRouter request failed: {exc}") from exc

    try:
        choice = provider["choices"][0]
        if choice.get("error"):
            raise AdapterError(f"provider failure: {choice['error']}")
        content = choice["message"]["content"]
        result = json.loads(content)
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        raise AdapterError(f"malformed OpenRouter response: {exc}") from exc
    if not isinstance(result, dict):
        raise AdapterError("structured response is not an object")
    result["_adapter"] = {
        "provider": "openrouter",
        "requested_model": MODEL,
        "reported_model": provider.get("model"),
        "request_id": provider.get("id"),
        "usage": provider.get("usage", {}),
        "reported_cost": provider.get("usage", {}).get("cost"),
    }
    return result


def main() -> int:
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict):
            raise AdapterError("request must be a JSON object")
        json.dump(call_openrouter(request), sys.stdout)
        sys.stdout.write("\n")
        return 0
    except (AdapterError, json.JSONDecodeError) as exc:
        print(f"INFRA_ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
