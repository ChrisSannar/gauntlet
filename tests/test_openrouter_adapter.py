from __future__ import annotations

import io
import json
import os
import unittest
from unittest.mock import patch

from controller.openrouter_adapter import AdapterError, MODEL, call_openrouter


class FakeResponse:
    def __init__(self, value: dict) -> None:
        self.value = value

    def __enter__(self):
        return io.BytesIO(json.dumps(self.value).encode())

    def __exit__(self, *args):
        return False


class OpenRouterAdapterTests(unittest.TestCase):
    @patch.dict(os.environ, {}, clear=True)
    def test_missing_key_is_infrastructure_error(self) -> None:
        with self.assertRaisesRegex(AdapterError, "OPENROUTER_API_KEY"):
            call_openrouter({"operation": "grade-day"})

    @patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"})
    @patch("controller.openrouter_adapter.urllib.request.urlopen")
    def test_returns_structured_result_and_audit_metadata(self, urlopen) -> None:
        urlopen.return_value = FakeResponse(
            {
                "id": "generation-1",
                "model": MODEL,
                "choices": [{"message": {"content": json.dumps({
                    "delivery_score": 3,
                    "mastery_score": 2.5,
                    "confidence": "high",
                    "summary": "fixture",
                    "evidence_citations": ["checks.unit"],
                    "strengths": ["The unit check passes."],
                    "improvement_actions": ["Add a failure-path test.", "Explain the state transition."],
                    "learning_directions": ["Rebuild the path from memory and verify it with a trace."],
                })}}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15, "cost": 0.01},
            }
        )
        result = call_openrouter({"operation": "grade-day", "evidence": {}})
        self.assertEqual(result["delivery_score"], 3)
        self.assertEqual(result["_adapter"]["reported_cost"], 0.01)
        sent = json.loads(urlopen.call_args.args[0].data)
        self.assertEqual(sent["model"], MODEL)
        self.assertEqual(sent["response_format"]["type"], "json_schema")


if __name__ == "__main__":
    unittest.main()
