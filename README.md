# Package & Dependency Management Skill

> Dependency health for AI agents — lookup packages, check versions, review changelogs, assess compatibility, analyze lockfiles, and generate safe upgrade plans via mcp-package-registry.

[![Skill Standard](https://img.shields.io/badge/standard-agentskills.io-blue)](https://agentskills.io)
[![MCP Server](https://img.shields.io/badge/mcp--server-mcp--package--registry-green)](https://github.com/zavora-ai/mcp-package-registry)
[![ADK-Rust Enterprise](https://img.shields.io/badge/ADK--Rust-Enterprise-purple.svg)](https://enterprise.adk-rust.com)
[![License](https://img.shields.io/badge/license-Apache--2.0-orange)](LICENSE)

## What This Skill Does

| Workflow | Tool Calls | What It Achieves |
|----------|-----------|------------------|
| Safe Upgrade Plan | 3 | Lockfile → prioritize → compatibility check |
| Changelog Review | 2 | Versions → what changed |
| Advisory Check | 1 | Vulnerable dependencies |

## Installation

```bash
git clone https://github.com/zavora-ai/skill-package-dependency-management.git \
  ~/.skills/skills/package-dependency-management
```

## Requirements

**Required:** `mcp-package-registry` (7 tools)

**Cross-MCP:**
- `mcp-security-advisory` — vulnerability-driven upgrades
- `mcp-github` — create upgrade PRs
- `mcp-cicd` — verify CI after upgrades

## Folder Structure

```
package-dependency-management/
├── SKILL.md                       # Decision tree + upgrade strategy
├── scripts/
│   └── upgrade_plan.py            # Prioritized upgrade plan generator
├── references/
│   ├── tool-sequences.md          # 7 tools
│   ├── cross-mcp-workflows.md     # Packages + Security + GitHub + CI/CD
│   └── examples.md                # Audit, upgrade, changelog
├── README.md
└── LICENSE
```

## Scripts

### `upgrade_plan.py`
```bash
python scripts/upgrade_plan.py '[{"name": "serde", "current": "1.0.190", "latest": "1.0.200", "has_advisory": true}]'
# → [{"package": "serde", "priority": "critical", "action": "upgrade_immediately"}]
```

## Contributors

| [<img src="https://github.com/jkmaina.png" width="80px;"/><br /><sub><b>James Karanja Maina</b></sub>](https://github.com/jkmaina) |
|:---:|

## License

Apache-2.0 — Part of [ADK-Rust Enterprise](https://enterprise.adk-rust.com). Built with ❤️ by [Zavora AI](https://zavora.ai)

## How It Works

### Security-First Upgrade Strategy

1. **Scan** — analyze lockfile for outdated + vulnerable deps
2. **Prioritize** — security fixes first, then major, then minor
3. **Check** — verify compatibility before upgrading
4. **Plan** — generate ordered upgrade path with breaking change warnings

## Success Criteria

| Metric | Target |
|--------|--------|
| Security priority | Vulnerable deps upgraded first |
| Safe upgrades | Changelog + compatibility checked before every upgrade |
| No floating ranges | Exact versions pinned in production |
