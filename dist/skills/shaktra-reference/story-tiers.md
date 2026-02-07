# Story Tiers

4-tier classification system for user stories. Tier determines required fields, quality gates, and coverage thresholds. Full story YAML schema is defined in the shaktra-stories skill — this file defines only the tier matrix.

## Tier Summary

| Tier | Typical Scope | Required Fields | Coverage Threshold | Check Depth |
|---|---|---|---|---|
| **Trivial** | Typo fix, config change, docs update | 3 | `settings.tdd.hotfix_coverage_threshold` | Quick |
| **Small** | Single-function change, minor bugfix | 5 | 80% | Quick |
| **Medium** | Feature addition, multi-file change | 10 | `settings.tdd.coverage_threshold` | Full |
| **Large** | Cross-cutting feature, architectural change | 15+ | 95% | Thorough |

## Auto-Detection Logic

```
if story has no acceptance criteria AND estimated_hours <= 1:
    tier = Trivial
else if files_touched <= 3 AND no new public API:
    tier = Small
else if files_touched <= 10 OR new public API:
    tier = Medium
else:
    tier = Large
```

The auto-detected tier is a suggestion. The user or TPM can override it explicitly in the story file.

## Required Fields Per Tier

**Trivial (3 fields):** title, description, acceptance_criteria

**Small (5 fields):** title, description, acceptance_criteria, affected_files, test_approach

**Medium (10 fields):** title, description, acceptance_criteria, affected_files, test_approach, dependencies, design_notes, error_handling, edge_cases, rollback_plan

**Large (15+ fields):** All Medium fields plus: architecture_impact, performance_considerations, security_review, migration_plan, monitoring_plan

## Gate Behavior Matrix

| Gate | Trivial | Small | Medium | Large |
|---|---|---|---|---|
| Failing test before code (Red) | Skip | Required | Required | Required |
| Tests pass after code (Green) | Required | Required | Required | Required |
| Refactor phase | Skip | Optional | Required | Required |
| Coverage threshold | `settings.tdd.hotfix_coverage_threshold` | 80% | `settings.tdd.coverage_threshold` | 95% |
| Quality check depth | Quick | Quick | Full | Thorough |
| Design review | Skip | Skip | Required | Required |
| PR review | Skip | Required | Required | Required |

## Check Depth Definitions

**Quick (~15 checks):** High-impact checks only — P0 triggers across all dimensions, critical error handling, security basics. Used for Trivial and Small tiers.

**Full (~35 checks):** Quick checks plus maintainability, observability, testing completeness, and configuration review. Used for Medium tier.

**Thorough (full + expanded):** Full checks plus architecture impact analysis, performance profiling review, dependency audit, and cross-cutting concern validation. Used for Large tier.
