#!/usr/bin/env python3
"""Technical decision framework."""
import json
def decide(): return {"frameworks": ["adr", "rfc", "tech_radar"], "criteria": ["feasibility", "scale", "maintainability"]}
if __name__ == "__main__": print(json.dumps(decide(), indent=2))
