## 1. Remove Collections

- [x] 1.1 Remove collection model and admin registration
- [x] 1.2 Clean up existing collection migration or create new removal migration

## 2. Introduce Favorites Model

- [x] 2.1 Create new `Favorite` model with `user`, `post`, and `saved_at`
- [x] 2.2 Set unique constraint `unique_together` for user/post
- [x] 2.3 Generate and apply migration for new model

## 3. Logic and Endpoints

- [x] 3.1 Provide toggle logic for adding/removing favorites
- [x] 3.2 Set up POST endpoint for toggling a favorite
- [x] 3.3 Ensure GET endpoint for profile favorites view

## 4. UI and Sorting

- [x] 4.1 Add private favorites list to profile view
- [x] 4.2 Implement sorting by `-saved_at`
- [x] 4.3 Make favorite button/action visible on posts

## 5. Verification

- [x] 5.1 Update or add existing tests
- [x] 5.2 Check migration and app runtime
