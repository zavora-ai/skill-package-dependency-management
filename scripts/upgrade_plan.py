#!/usr/bin/env python3
"""Generate prioritized upgrade plan from outdated dependencies."""
import json, sys

def plan(deps):
    upgrades = []
    for dep in deps:
        priority = "critical" if dep.get("has_advisory") else "high" if dep.get("major_behind", 0) > 0 else "normal"
        upgrades.append({
            "package": dep["name"],
            "current": dep.get("current", "?"),
            "latest": dep.get("latest", "?"),
            "priority": priority,
            "breaking": dep.get("major_behind", 0) > 0,
            "action": "upgrade_immediately" if priority == "critical" else "plan_upgrade" if dep.get("major_behind", 0) > 0 else "safe_upgrade",
        })
    return sorted(upgrades, key=lambda x: {"critical": 0, "high": 1, "normal": 2}[x["priority"]])

if __name__ == "__main__":
    print(json.dumps(plan(json.loads(sys.argv[1])), indent=2))
