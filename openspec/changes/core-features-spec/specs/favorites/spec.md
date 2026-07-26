## ADDED Requirements

### Requirement: Add post to favorites
The system SHALL allow users to save posts to their private favorites list.

#### Scenario: Save as favorite
- **WHEN** a user clicks the favorite button on a post
- **THEN** the post is added to their favorites list

### Requirement: Remove post from favorites
The system SHALL allow users to remove posts from their favorites list.

#### Scenario: Remove from favorites
- **WHEN** a user clicks the unfavorite button on a favorited post
- **THEN** the post is removed from their favorites list

### Requirement: View own favorites
The system SHALL display the user's favorites on their profile.

#### Scenario: Favorites list
- **WHEN** a user views their own favorites page
- **THEN** all favorited posts are displayed sorted by most recently saved

### Requirement: Favorites are private
The system SHALL make favorites visible only to the owner.

#### Scenario: Private favorites
- **WHEN** another user views someone's profile
- **THEN** the favorites list is not visible