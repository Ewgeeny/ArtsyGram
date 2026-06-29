## Why

The ArtsyGram project has minimal agentic infrastructure: AGENTS.md contains basic Django conventions but lacks project-specific detail, no `opencode.json` config exists, and the OpenSpec `config.yaml` is a near-empty template. Without a proper setup, AI agents lack the context needed to work effectively and consistently, leading to wasted effort, convention drift, and misaligned code.

## What Changes

- **AGENTS.md audit and enrichment** — Review the existing file, fill in gaps (detailed project structure, code style, branch/commit conventions, testing commands, linting instructions), and keep it concise and actionable.
- **Create `opencode.json`** — Register custom commands, modes, and agent instructions that match the project's Django architecture. This is the primary way opencode learns about the project.
- **Fill OpenSpec `config.yaml` context and rules** — Add project context (tech stack, domain) and per-artifact rules so generated artifacts are consistently high quality.
- **Rationalize skill/command layout** — The `.opencode/skills/` and `.opencode/commands/` directories exist but lack supporting configuration. Ensure they're properly wired and referenced.
- **Add `OPENCODE.md` or enhance `AGENTS.md`** — Ensure agents have a clear, single source of truth about how to work in this project.

## Capabilities

### New Capabilities
- `agentic-config`: Project-level opencode configuration (`opencode.json`) that registers custom commands, modes, and agent behavior tailored to Django development.
- `spec-infrastructure`: Filled-in OpenSpec context and rules in `config.yaml`, plus initial spec stubs for the main app domains.

### Modified Capabilities
None — no existing specs to modify.

## Impact

- **AGENTS.md** — rewritten for clarity and completeness
- **opencode.json** — new file at project root
- **openspec/config.yaml** — context and rules populated
- **.opencode/ commands and skills** — verified to be correct and referenced
