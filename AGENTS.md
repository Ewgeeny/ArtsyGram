# AGENTS.md

## Project scope

This is a Django app for sharing and managing creative inspiration through image-based posts.

Main app:

- `core` — models, views, forms, templates and services for the entire application

Key features:

- User registration, login and profiles
- Image posts with categories and tags
- Tag-based filtering on the main page
- Private favorites list (add/remove posts, view on profile)
- Edit and delete posts (own posts only)

## Important project conventions

- Put business logic in `services.py`, not in views.
- Keep views simple and reusable.
- Use Django ORM instead of raw SQL.
- Follow the existing project structure.

## Commands

- Run server: `python manage.py runserver`
- Run tests: `python manage.py test`
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`

## Things that are easy to break

- User authentication
- Image uploads
- Search and filtering
- Relationships between posts, tags and categories
- Favorites (unique constraint per user/post)

## Change coupling

If you change:

- a model → also check forms, admin and related views
- authentication → also check permissions and user profiles
- categories or tags → also check search and filtering
- favorites → also check profile view and toggle endpoint

## Constraints

- Do not edit old migrations; create a new one instead.
- Do not rename URL names unless explicitly asked.
- Prefer small, targeted changes over broad refactors.

## Documentation use

- Keep project documentation up to date.
- Report inconsistencies between documentation and implementation.
- Update documentation when new functionality is added.

## Testing expectations

Add or update tests for:

- authentication
- model changes
- image uploads
- search functionality
- CRUD operations for posts
- favorites toggle logic