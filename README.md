# Artsy Gram

Artsy Gram is a creative inspiration and photo-sharing web application developed as part of the Web Engineering course.

## Description

Users can upload image-based posts related to art, fashion, photography, interior design, and other creative fields. The application allows browsing, searching, and organizing creative inspiration.

## Features

- User registration and login
- Upload image posts with categories and tags
- Search and filter by tags and categories
- User profiles with post listings
- Private favorites list (add/remove posts, view on profile)
- Edit and delete posts (own posts only)

## Project Structure

```
ArtsyGram/
├── artsygram/          # Project settings and URL configuration
├── core/               # Main application
│   ├── models.py       # Database models (Post, Category, Tag, Favorite)
│   ├── views.py        # View functions
│   ├── forms.py        # Django forms
│   ├── services.py     # Business logic
│   └── templates/      # HTML templates
└── manage.py           # Django management script
```

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Apply migrations:
   ```bash
   uv run python manage.py migrate
   ```
4. Create a superuser (optional):
   ```bash
   uv run python manage.py createsuperuser
   ```
5. Run the development server:
   ```bash
   uv run python manage.py runserver
   ```

## Production Deployment

This project is set up to run in a production-like environment locally using **Uvicorn** as the ASGI application server and **nginx** as a reverse proxy.

### Deployment Decisions

- **Hosting:** Local machine, accessed via local network or localhost
- **Application Server:** Uvicorn (ASGI), started with `uv run uvicorn artsygram.asgi:application`
- **Reverse Proxy:** nginx, forwards requests to Uvicorn and serves static/media files directly
- **Static Files:** Django `collectstatic` collects all static files (CSS, JS) into `static-prod/`. nginx serves them directly from that directory. WhiteNoise middleware acts as a fallback.
- **Media Files:** Uploaded images are stored in the `media/` directory on disk. nginx serves them directly. Since the database and media directory are local, uploads persist across server restarts.

### Production Setup

Install the project dependencies:

```bash
uv sync
```

Apply database migrations:

```bash
uv run python manage.py migrate
```

Collect all static files:

```bash
uv run python manage.py collectstatic
```

Start the application using the production application server:

```bash
uv run uvicorn artsygram.asgi:application --host 127.0.0.1 --port 8000
```

The application will be available at `http://127.0.0.1:8000` (uvicorn directly) or through nginx on its configured port.

### Environment Variables

The following environment variables should be configured:

```
SECRET_KEY=<your-secret-key>
DEBUG=False
```

## URL Structure

- `/` - Welcome page with login/registration
- `/main/` - Main page with posts and filtering
- `/profile/<username>/` - User profile with posts
- `/profile/<username>/favorites/` - User's private favorites
- `/posts/create/` - Create new post
- `/posts/<id>/edit/` - Edit post
- `/posts/<id>/delete/` - Delete post
- `/posts/<id>/favorite/` - Toggle favorite
- `/admin/` - Django admin interface

## Testing

Run tests with:
```bash
python manage.py test
```

## Technologies

- Django 6.0.6
- Python 3.14
- SQLite
- HTML/CSS
- HTMX
- WhiteNoise
- Uvicorn

## Author

Ewgenia Sterleadova