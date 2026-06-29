## 1. Audit Current State

- [ ] 1.1 Read and evaluate current AGENTS.md for gaps
- [ ] 1.2 Check `.opencode/` directory for dead or orphaned files
- [ ] 1.3 Verify OpenSpec `config.yaml` content and identify missing fields
- [ ] 1.4 Check if `opencode.json` has ever been created (search git history)

## 2. Create opencode.json

- [ ] 2.1 Create `opencode.json` at the repo root with `customCommands`, `customModes`, and `agentInstructions` sections
- [ ] 2.2 Register custom commands: `dev` (runserver), `test` (manage.py test), `migrate`, `makemigrations`
- [ ] 2.3 Register a "Django developer" custom mode with relevant file globs (`apps/**/*.py`, `templates/**/*.html`, etc.) and agent instructions
- [ ] 2.4 Verify `opencode.json` is valid JSON and opencode loads it without errors

## 3. Rewrite AGENTS.md

- [ ] 3.1 Add detailed project structure overview (apps directory, key files)
- [ ] 3.2 Add code style guidelines (Python conventions, naming, imports)
- [ ] 3.3 Add branch/commit conventions if applicable
- [ ] 3.4 Add testing instructions and linting/formatting commands
- [ ] 3.5 Remove any outdated or incorrect content
- [ ] 3.6 Cross-reference with opencode.json to avoid duplication

## 4. Populate OpenSpec Config

- [ ] 4.1 Add `context` field to `openspec/config.yaml` with tech stack (Python 3.14, Django, uv), project domain, and conventions
- [ ] 4.2 Add per-artifact `rules` for proposal, design, specs, and tasks
- [ ] 4.3 Validate config.yaml with `openspec validate`

## 5. Clean Up .opencode/ Directory

- [ ] 5.1 Review `.opencode/commands/` markdown files — remove if dead, keep if they serve a purpose
- [ ] 5.2 Review `.opencode/skills/` — verify each SKILL.md is accurate and referenced
- [ ] 5.3 Remove node_modules/ and package files from .opencode/ tracking if not needed

## 6. Final Validation

- [ ] 6.1 Run `openspec doctor` to verify overall OpenSpec setup health
- [ ] 6.2 Confirm `opencode` CLI reports the project correctly
- [ ] 6.3 Commit all changes with a descriptive message
