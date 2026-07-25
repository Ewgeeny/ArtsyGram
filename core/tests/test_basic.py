"""Tests for favorite models and services."""

from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Category, Favorite, Post
from core.services import toggle_favorite


class FavoriteModelTest(TestCase):
    """Tests for the Favorite model."""

    def setUp(self):
        """Create a user, category, and post for the tests."""
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.category = Category.objects.create(name="testcategory")
        self.post = Post.objects.create(
            user=self.user,
            title="Test Post",
            description="Test description",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

    def test_create_favorite(self):
        """Verify that a favorite stores the correct user and post."""
        favorite = Favorite.objects.create(
            user=self.user,
            post=self.post,
        )

        self.assertEqual(favorite.user, self.user)
        self.assertEqual(favorite.post, self.post)

    def test_unique_together(self):
        """Verify that a user cannot favorite the same post twice."""
        Favorite.objects.create(
            user=self.user,
            post=self.post,
        )

        with self.assertRaises(Exception):
            Favorite.objects.create(
                user=self.user,
                post=self.post,
            )


class ToggleFavoriteTest(TestCase):
    """Tests for the toggle_favorite service."""

    def setUp(self):
        """Create a user, category, and post for the tests."""
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
        )
        self.category = Category.objects.create(name="testcategory")
        self.post = Post.objects.create(
            user=self.user,
            title="Test Post",
            description="Test description",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

    def test_add_favorite(self):
        """Verify that toggle_favorite creates a favorite."""
        result = toggle_favorite(self.user, self.post)

        self.assertTrue(result)
        self.assertTrue(
            Favorite.objects.filter(
                user=self.user,
                post=self.post,
            ).exists()
        )

    def test_remove_favorite(self):
        """Verify that toggle_favorite removes an existing favorite."""
        toggle_favorite(self.user, self.post)

        result = toggle_favorite(self.user, self.post)

        self.assertFalse(result)
        self.assertFalse(
            Favorite.objects.filter(
                user=self.user,
                post=self.post,
            ).exists()
        )
