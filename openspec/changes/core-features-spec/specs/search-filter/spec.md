## ADDED Requirements

### Requirement: Filter by category
The system SHALL allow users to filter posts by category.

#### Scenario: Category filtering
- **WHEN** a user selects a category from the filter
- **THEN** only posts in that category are displayed

### Requirement: Filter by tag
The system SHALL allow users to filter posts by tag name.

#### Scenario: Tag filtering
- **WHEN** a user enters a tag name in the filter
- **THEN** only posts with that tag are displayed

### Requirement: Combined filtering
The system SHALL support filtering by both category and tag simultaneously.

#### Scenario: Multiple filters
- **WHEN** a user applies both category and tag filters
- **THEN** only posts matching both criteria are displayed