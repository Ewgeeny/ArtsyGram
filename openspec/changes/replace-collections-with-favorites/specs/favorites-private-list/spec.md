## ADDED Requirements

### Requirement: User can save post to private favorites
The system SHALL allow users to add a post to their private favorites list.

#### Scenario: Save a post as favorite
- **WHEN** a user marks a post as favorite
- **THEN** the post is added to their private favorites list

### Requirement: User can remove post from private favorites
The system SHALL allow users to remove a post from their private favorites list.

#### Scenario: Remove a post from favorites
- **WHEN** a user removes a favorite
- **THEN** the post is deleted from their favorites list

### Requirement: Profile shows own favorites sorted by newest saved first
The system SHALL display the user's own favorites list on the profile sorted by save time, most recently saved first.

#### Scenario: Favorites order on profile
- **WHEN** the profile page with favorites is loaded
- **THEN** entries are displayed in order of newest save time first

### Requirement: Favorites list is private
The system SHALL make the favorites list visible only to the user themselves.

#### Scenario: Other users cannot view favorites
- **WHEN** another user views the profile
- **THEN** no favorites are displayed
