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
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
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

- Django 5.1
- Python 3.12
- SQLite (default database)
- HTML/CSS/JavaScript
- HTMX for dynamic interactions

## Author

Ewgenia Sterleadova