#!/usr/bin/env python3
"""Team dynamics analyzer."""
import json
def analyze(): return {"stages": ["forming", "storming", "norming", "performing"], "health": ["safety", "trust", "accountability"]}
if __name__ == "__main__": print(json.dumps(analyze(), indent=2))
