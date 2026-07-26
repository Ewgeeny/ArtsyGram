## ADDED Requirements

### Requirement: Create post
The system SHALL allow authenticated users to create new image posts.

#### Scenario: Successful post creation
- **WHEN** a user submits a valid post with title, image, description, and category
- **THEN** the post is created and the user is redirected to their profile

### Requirement: Edit post
The system SHALL allow users to edit their own posts.

#### Scenario: Successful post edit
- **WHEN** a user edits their own post with valid data
- **THEN** the post is updated and the user is redirected to their profile

### Requirement: Delete post
The system SHALL allow users to delete their own posts.

#### Scenario: Successful post deletion
- **WHEN** a user confirms deletion of their own post
- **THEN** the post is removed and the user is redirected to their profile

### Requirement: Post ownership
The system SHALL only allow users to modify their own posts.

#### Scenario: Unauthorized modification blocked
- **WHEN** a user tries to edit or delete another user's post
- **THEN** the action is rejected and the user is redirected