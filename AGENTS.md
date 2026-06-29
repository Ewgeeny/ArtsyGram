# AGENTS.md

## Project scope

This is a Django app for sharing and managing creative inspiration through image-based posts.

Main apps:

- `apps/accounts` — user registration, login and profiles
- `apps/posts` — image posts and post management
- `apps/search` — searching and filtering posts
- `apps/collections` — saved inspiration boards (optional)
- `apps/web` — server-rendered user interface

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

## Change coupling

If you change:

- a model → also check forms, admin and related views
- authentication → also check permissions and user profiles
- categories or tags → also check search and filtering
- collections → also check saved posts

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