## ADDED Requirements

### Requirement: Post categories
The system SHALL organize posts into categories.

#### Scenario: Category assignment
- **WHEN** a user creates or edits a post
- **THEN** the user must select one category for the post

### Requirement: Post tags
The system SHALL allow posts to have multiple tags.

#### Scenario: Tag assignment
- **WHEN** a user creates or edits a post
- **THEN** the user can add multiple tags separated by spaces

### Requirement: Tag creation
The system SHALL automatically create new tags when needed.

#### Scenario: New tag handling
- **WHEN** a user enters a tag name that doesn't exist
- **THEN** a new tag is created and assigned to the post