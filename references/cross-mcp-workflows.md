# Package Cross-MCP Workflows

## Packages + Security: Vulnerability-Driven Upgrades
```
SECURITY: audit_dependencies(manifest: "Cargo.lock") → vulnerable packages
PACKAGES: propose_upgrades(strategy: "security_first") → upgrade plan
PACKAGES: check_compatibility(package, from, to) → breaking changes?
GITHUB: create_pull_request(title: "fix(deps): security upgrades")
```

## Packages + CI/CD: Verify After Upgrade
```
PACKAGES: propose_upgrades() → plan
GITHUB: create_branch(branch: "chore/dep-upgrades")
CICD: list_pipeline_runs(branch: "chore/dep-upgrades") → verify CI passes
TESTS: run_unit_tests() → confirm no regressions
```
