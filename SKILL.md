---
name: package-dependency-management
description: Manage package dependencies — lookup packages, check versions, review changelogs, assess compatibility, analyze lockfiles, and propose upgrades. Use when updating dependencies, checking for outdated packages, planning major upgrades, reviewing changelogs, or auditing dependency health.
version: "1.0.0"
license: Apache-2.0
allowed-tools: [lookup_package, list_versions, get_changelog, check_advisories, check_compatibility, analyze_lockfile, propose_upgrades]
tags: [devops, dependencies, packages, upgrades, maintenance]
metadata:
  author: Zavora AI
  mcp-server: mcp-package-registry
  success-criteria:
    trigger-rate: "90% on dependency queries"
    safe-upgrades: "Always check changelog + compatibility before upgrading"
---

# Package & Dependency Management

You manage dependencies safely. Check changelogs before upgrading, verify compatibility, and prioritize security fixes over feature upgrades.

## Decision Tree
```
├── "outdated", "update", "upgrade"? → analyze_lockfile + propose_upgrades
├── "changelog", "what changed"? → get_changelog
├── "compatible", "will it break"? → check_compatibility
├── "vulnerable", "advisory"? → check_advisories
├── "info", "about package"? → lookup_package / list_versions
```

## Key Workflows

### Safe Upgrade Plan (3 calls)
1. `analyze_lockfile(path: "Cargo.lock")` → outdated + vulnerable deps
2. `propose_upgrades(strategy: "security_first")` → prioritized upgrade plan
3. `check_compatibility(package, from_version, to_version)` → breaking changes?

### Changelog Review (2 calls)
1. `list_versions(package: "serde")` → all versions
2. `get_changelog(package: "serde", from: "1.0.190", to: "1.0.200")` → what changed

## MUST DO
- Review changelogs for breaking changes before major upgrades
- Prioritize security advisories over feature upgrades
- Pin exact versions in production
- Check transitive dependency impact

## MUST NOT DO
- Never upgrade production deps without testing
- Don't use floating version ranges in production
- Don't ignore breaking change warnings
