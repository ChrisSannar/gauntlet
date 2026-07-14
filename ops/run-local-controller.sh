#!/usr/bin/env bash
set -euo pipefail

exec /usr/bin/bash -ic \
  'exec python /home/chrissannar/Practice/gauntlet/controller/gauntlet_controller.py close-auto /home/chrissannar/Practice/gauntlet/runs/2026-07-15-tutoring-platform/run.json --state-dir /home/chrissannar/.local/state/gauntlet'
