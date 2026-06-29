## Context

The current agentic setup is fragmented. AGENTS.md lives at the project root with basic Django conventions. `.opencode/` contains skill and command files but has no top-level `opencode.json` to wire them together. The OpenSpec `config.yaml` is empty. AI agents have no structured project context beyond the generic AGENTS.md content.

This design covers the three layers of agentic infrastructure:
1. **opencode.json** — The primary configuration file for opencode CLI
2. **AGENTS.md** — Human-readable instructions for AI agents
3. **openspec/config.yaml** — OpenSpec project context and artifact rules

## Goals / Non-Goals

**Goals:**
- Create a well-structured `opencode.json` that registers custom commands, modes, and agent instructions
- Rewrite AGENTS.md to be accurate, comprehensive, and actionable
- Populate `openspec/config.yaml` with project context and artifact rules
- Ensure all three files are consistent and reference each other
- Remove the generic `.opencode/commands/` markdown files if they're dead weight (unless they serve a purpose)

**Non-Goals:**
- Not changing any application code or Django configuration
- Not adding new Django apps or models
- Not creating comprehensive specs for all capabilities — only spec infrastructure

## Decisions

1. **opencode.json as the single source of truth for opencode behavior** — Rather than splitting config across files, `opencode.json` will define custom commands, modes, and agent instructions. AGENTS.md will remain as the human-readable entry point.

2. **Flat structure for opencode.json** — Use `customCommands`, `customModes`, and `agentInstructions` at the top level. No nested indirection.

3. **Django-aware custom modes** — Register custom modes for "Django developer" that include the relevant file globs and instructions from AGENTS.md.

4. **AGENTS.md kept, not removed** — It serves as a quick reference for humans and AI agents that don't read opencode.json. Content will be deduplicated with opencode.json.

5. **Config.yaml context aligned with AGENTS.md** — The OpenSpec `context` field will mirror the project scope from AGENTS.md so specs are generated with the right domain knowledge.

## Risks / Trade-offs

- **[Risk] Duplication between opencode.json and AGENTS.md** → AGENTS.md is the concise human version; opencode.json is the structured machine version. Keep AGENTS.md as a subset.
- **[Risk] Over-configuration** → Start minimal (custom modes + commands) and add as needed. Avoid premature optimization.
- **[Risk] Breaking existing agent behavior** → The current setup is minimal, so the surface area of "breaking" is near zero. Validate by running `opencode` after changes.
