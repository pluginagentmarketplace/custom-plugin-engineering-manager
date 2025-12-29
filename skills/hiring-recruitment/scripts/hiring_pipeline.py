#!/usr/bin/env python3
"""Hiring pipeline tracker."""
import json
def pipeline(): return {"stages": ["source", "screen", "interview", "offer", "close"], "interviews": ["technical", "behavioral", "design"]}
if __name__ == "__main__": print(json.dumps(pipeline(), indent=2))
