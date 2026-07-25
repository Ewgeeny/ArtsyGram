"""Tests for model __str__ methods."""

from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Category, Favorite, Post, Tag


class CategoryStrTest(TestCase):
    """Tests for the Category string representation."""

    def test_str(self):
        """Verify that Category.__str__ returns the category name."""
        category = Category.objects.create(name="Landscape")

        self.assertEqual(str(category), "Landscape")


class TagStrTest(TestCase):
    """Tests for the Tag string representation."""

    def test_str(self):
        """Verify that Tag.__str__ returns the tag name."""
        tag = Tag.objects.create(name="sunset")

        self.assertEqual(str(tag), "sunset")


class PostStrTest(TestCase):
    """Tests for the Post string representation."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")

    def test_str(self):
        """Verify that Post.__str__ returns the post title."""
        post = Post.objects.create(
            user=self.user,
            title="My Artwork",
            description="A painting",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

        self.assertEqual(str(post), "My Artwork")


class FavoriteStrTest(TestCase):
    """Tests for the Favorite string representation."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="bob",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.post = Post.objects.create(
            user=self.user,
            title="Cool Painting",
            description="Beautiful",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

    def test_str(self):
        """Verify that Favorite.__str__ returns the expected string."""
        favorite = Favorite.objects.create(
            user=self.user,
            post=self.post,
        )

        self.assertEqual(
            str(favorite),
            "bob - Cool Painting",
        )
