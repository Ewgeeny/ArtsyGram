## ADDED Requirements

### Requirement: OpenSpec config.yaml context
The `openspec/config.yaml` file SHALL contain a `context` field describing the project's tech stack, domain, and conventions so that AI-generated artifacts are consistent with the project.

#### Scenario: Context field populated
- **WHEN** OpenSpec generates new artifacts for this project
- **THEN** the `context` field from `config.yaml` SHALL be included as background context for AI agents

### Requirement: OpenSpec config.yaml rules
The `openspec/config.yaml` file SHALL contain per-artifact rules that guide the structure and quality of generated proposals, designs, specs, and tasks.

#### Scenario: Proposal rules applied
- **WHEN** a proposal artifact is generated
- **THEN** the proposal rules from `config.yaml` SHALL be enforced

#### Scenario: Tasks rules applied
- **WHEN** a tasks artifact is generated
- **THEN** the tasks rules from `config.yaml` SHALL be enforced

### Requirement: OpenSpec specs directory stubbed
The `openspec/specs/` directory SHALL contain initial spec stubs for the main app domains (accounts, posts, search, collections, web) to document existing system behavior.

#### Scenario: Spec stubs created
- **WHEN** a developer inspects `openspec/specs/`
- **THEN** they SHALL find a directory for each main Django app with at least an empty or placeholder spec.md
