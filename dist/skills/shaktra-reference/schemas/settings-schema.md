# Settings Schema

Defines `.shaktra/settings.yml` — the single configuration file for all Shaktra thresholds and project metadata. Every threshold in the framework reads from this file; none are hardcoded.

## Schema

```yaml
project:
  name: string            # required — project display name
  type: string            # "greenfield" | "brownfield"
  language: string        # "python" | "typescript" | "go" | "java" | "rust" | etc.
  test_framework: string  # "pytest" | "jest" | "vitest" | "go test" | etc.
  coverage_tool: string   # "coverage" | "istanbul" | "c8" | etc.
  package_manager: string # "pip" | "npm" | "pnpm" | "cargo" | etc.

tdd:
  coverage_threshold: integer       # default: 90 — Medium tier target
  hotfix_coverage_threshold: integer # default: 70 — Trivial tier target

quality:
  p1_threshold: integer  # default: 2 — max P1 findings before merge block

review:
  verification_test_persistence: string  # default: "ask" — "auto" | "always" | "never" | "ask"
  min_verification_tests: integer        # default: 5 — minimum independent verification tests

analysis:
  summary_token_budget: integer  # default: 600 — max tokens per artifact summary section
  incremental_refresh: boolean   # default: true — enable checksum-based incremental refresh

sprints:
  enabled: boolean              # default: true
  velocity_tracking: boolean    # default: true
  sprint_duration_weeks: integer # default: 2
```

## Consumer Reference

| Setting | Read By |
|---|---|
| `project.*` | init skill (writes), all agents (context) |
| `tdd.coverage_threshold` | sw-quality, test-agent, story-tiers gate matrix |
| `tdd.hotfix_coverage_threshold` | sw-quality, test-agent, story-tiers gate matrix |
| `quality.p1_threshold` | sw-quality, code-reviewer, severity-taxonomy merge gate |
| `review.verification_test_persistence` | code-reviewer |
| `review.min_verification_tests` | code-reviewer |
| `analysis.summary_token_budget` | cba-analyzer, analyze skill (validation) |
| `analysis.incremental_refresh` | analyze skill (refresh workflow) |
| `sprints.enabled` | scrummaster, tpm-quality |
| `sprints.velocity_tracking` | scrummaster |
| `sprints.sprint_duration_weeks` | scrummaster |
