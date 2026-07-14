## Why

The current collection-based approach does not fit the intended user flow. A private favorites list is needed instead, allowing users to save posts and view them on their profile sorted by save time.

## What Changes

- Removes existing collection functionality from models, admin, and related logic.
- Introduces a new Favorite entity as a private, user-specific collection.
- Enables saving and removing posts as favorites.
- Displays a private favorites list on the profile, sorted by most recently saved first.

## Capabilities

### New Capabilities

- `favorites-private-list`: Private favorites list with add/remove and profile view, sorted by save time (newest first).

### Modified Capabilities

- `collections-removal`: Removes existing collection functionality from UI and logic.

## Impact

- Affected code: Models, admin, views, templates, forms, and URL routing related to collections/favorites.
- Data migration: Existing collection data must be evaluated and migrated or removed.
- Side effects: Existing collection links/features are removed and replaced with profile favorites.
