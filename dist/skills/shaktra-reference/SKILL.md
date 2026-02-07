---
name: shaktra-reference
description: >
  Shared constants and quality standards for all Shaktra agents. Defines severity taxonomy,
  quality principles, guard tokens, story tiers, and review dimensions.
user-invocable: false
---

# Shaktra Reference — Single Source of Truth

This skill contains canonical definitions for the Shaktra framework. No other file may redefine the constants, taxonomies, or standards declared here. Agents and skills reference these files — they never duplicate them.

## Loading

Agents load this skill via their `skills` frontmatter. Only load the sub-files your agent actually needs.

## Sub-Files

| File | Purpose |
|---|---|
| `severity-taxonomy.md` | P0-P3 severity levels, examples, merge gate logic |
| `quality-principles.md` | 10 core principles with verification checks |
| `guard-tokens.md` | 15 structured tokens for phase/quality/workflow signaling |
| `story-tiers.md` | 4-tier story classification with field requirements and gates |
| `quality-dimensions.md` | 13 review dimensions (A-M) with key checks and P0 triggers |

## Agent Loading Guide

| Agent Role | Sub-Files Needed |
|---|---|
| SW Quality, Code Reviewer | severity-taxonomy, quality-principles, quality-dimensions |
| SW Engineer, Developer | severity-taxonomy, quality-principles, guard-tokens |
| Test Agent | severity-taxonomy, guard-tokens |
| TPM Quality, Scrum Master | story-tiers, guard-tokens |
| Architect | quality-principles, quality-dimensions |
