## Context

ArtsyGram is a Django-based web application for sharing creative inspiration through image posts. The application is already implemented with core features including user authentication, post management, categories/tags, search/filtering, user profiles, and favorites.

This design document formalizes the existing implementation as a reference for the Bachelor Web Engineering course evaluation.

## Goals / Non-Goals

**Goals:**
- Document the current architectural decisions
- Provide a reference for technical evaluation
- Establish baseline for future enhancements

**Non-Goals:**
- Propose new features or changes
- Refactor existing implementation
- Add new dependencies

## Decisions

### Framework Choice: Django
**Decision**: Use Django as the web framework.
**Rationale**: Django provides built-in authentication, ORM, admin interface, and follows MVC pattern suitable for rapid web development.
**Alternatives considered**: Flask (more lightweight but requires more boilerplate for authentication and ORM).

### Database: SQLite
**Decision**: Use SQLite as the default database.
**Rationale**: Suitable for development and small-scale deployment. Django's ORM allows easy migration to PostgreSQL/MySQL later.
**Alternatives considered**: PostgreSQL (better for production but overkill for course project).

### Authentication: Django's built-in auth
**Decision**: Use Django's built-in User model and authentication views.
**Rationale**: Provides secure password hashing, session management, and CSRF protection out of the box.
**Alternatives considered**: Custom authentication (more work, higher security risk).

### Image Storage: Django's MEDIA_ROOT
**Decision**: Store uploaded images in the filesystem under MEDIA_ROOT.
**Rationale**: Simple setup for development. For production, could migrate to cloud storage (S3, Cloudinary).
**Alternatives considered**: Cloud storage from start (adds complexity and cost).

### Tag Processing: Space-separated input
**Decision**: Parse tags from space-separated input in forms.
**Rationale**: Simple user interface, easy to implement. Tags are stored as separate Tag model entries with M2M relationship.
**Alternatives considered**: Comma-separated (more common but requires UI changes).

## Risks / Trade-offs

**[Risk] SQLite limitations** → Acceptable for course project; can migrate to PostgreSQL for production deployment.

**[Risk] File-based image storage** → Simple but not scalable; acceptable scope for Bachelor project.

**[Risk] No image validation** → Current implementation doesn't validate file type or size; could be added as future enhancement.

**[Trade-off] Simplicity vs. Features** → Chose simpler implementation (space-separated tags, no image processing) to meet course timeline.