#!/usr/bin/env python3
"""Employee engagement analyzer."""
import json
def survey(): return {"drivers": ["purpose", "autonomy", "mastery", "belonging"], "metrics": ["enps", "satisfaction", "retention"]}
if __name__ == "__main__": print(json.dumps(survey(), indent=2))
