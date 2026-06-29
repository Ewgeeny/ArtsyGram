## ADDED Requirements

### Requirement: opencode.json configuration
The project SHALL have an `opencode.json` file at the repository root that registers project-specific custom commands, custom modes, and agent instructions.

#### Scenario: Custom commands defined
- **WHEN** opencode loads the project
- **THEN** it SHALL discover custom commands defined in `opencode.json` and make them available to the user

#### Scenario: Custom modes defined
- **WHEN** opencode loads the project
- **THEN** it SHALL register custom modes from `opencode.json` with their associated file globs and instructions

#### Scenario: Agent instructions available
- **WHEN** an AI agent starts a session in this project
- **THEN** it SHALL receive the agent instructions defined in `opencode.json`

### Requirement: AGENTS.md maintained
The project SHALL keep AGENTS.md at the repository root as the human-readable entry point for project conventions, commands, and architecture overview.

#### Scenario: AGENTS.md is up to date
- **WHEN** project structure or conventions change
- **THEN** AGENTS.md SHALL be updated to reflect those changes

#### Scenario: AGENTS.md covers project essentials
- **WHEN** a developer or AI agent reads AGENTS.md
- **THEN** they SHALL find: project scope, app list, conventions, common commands, testing instructions, and change coupling guidance
