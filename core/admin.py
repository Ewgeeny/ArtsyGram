"""Admin configuration for the ArtsyGram application."""

from django.contrib import admin
from .models import Category, Tag, Post, Favorite

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Favorite)
