## ADDED Requirements

### Requirement: Remove collections feature
The system SHALL completely remove existing collection functionality.

#### Scenario: No collection UI or logic remains
- **WHEN** the app is used
- **THEN** there are no more collections, no related routes, views, or models

### Requirement: Clean up migration history
The system SHALL safely remove existing collection migration and model definition.

#### Scenario: Migration state is consistent
- **WHEN** the database is checked after the change
- **THEN** no collection model exists and there are no inconsistent migrations
