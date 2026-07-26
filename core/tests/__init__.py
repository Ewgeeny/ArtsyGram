"""Shared test fixtures for the core app."""

from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Category, Favorite, Post


class BaseTestCase(TestCase):
    """Shared setUp for tests that need a user, category, and post."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.post = Post.objects.create(
            user=self.user,
            title="Test Post",
            description="Test description",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )
        self.client.login(
            username="alice",
            password="pass1234",
        )

    def _create_user(self, username="bob"):
        """Create and return an additional user."""
        return User.objects.create_user(
            username=username,
            password="pass1234",
        )

    def _favorite_exists(self, user=None, post=None):
        """Return True if a Favorite exists for the given user and post."""
        return Favorite.objects.filter(
            user=user or self.user,
            post=post or self.post,
        ).exists()
