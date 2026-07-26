## ADDED Requirements

### Requirement: User registration
The system SHALL allow new users to create an account with username and password.

#### Scenario: Successful registration
- **WHEN** a visitor submits valid registration credentials
- **THEN** a new user account is created and the user is logged in

### Requirement: User login
The system SHALL allow registered users to log in with username and password.

#### Scenario: Successful login
- **WHEN** a user submits valid login credentials
- **THEN** the user is authenticated and redirected to the main page

### Requirement: User logout
The system SHALL allow logged-in users to log out.

#### Scenario: Successful logout
- **WHEN** a user clicks the logout button
- **THEN** the session is terminated and the user is redirected to the welcome page

### Requirement: Authentication required
The system SHALL require authentication for all protected pages.

#### Scenario: Unauthenticated access blocked
- **WHEN** a non-logged-in user tries to access a protected page
- **THEN** the user is redirected to the welcome page