#!/usr/bin/env python3
"""Performance review tracker."""
import json
def track(): return {"cycles": ["annual", "quarterly"], "metrics": ["goals", "growth", "impact", "collaboration"]}
if __name__ == "__main__": print(json.dumps(track(), indent=2))
