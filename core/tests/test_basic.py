"""Tests for favorite models and services."""

from core.models import Favorite
from core.services import toggle_favorite

from . import BaseTestCase


class FavoriteModelTest(BaseTestCase):
    """Tests for the Favorite model."""

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


class ToggleFavoriteTest(BaseTestCase):
    """Tests for the toggle_favorite service."""

    def test_add_favorite(self):
        """Verify that toggle_favorite creates a favorite."""
        result = toggle_favorite(self.user, self.post)

        self.assertTrue(result)
        self.assertTrue(self._favorite_exists())

    def test_remove_favorite(self):
        """Verify that toggle_favorite removes an existing favorite."""
        toggle_favorite(self.user, self.post)

        result = toggle_favorite(self.user, self.post)

        self.assertFalse(result)
        self.assertFalse(self._favorite_exists())
