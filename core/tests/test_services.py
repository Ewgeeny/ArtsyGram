"""Tests for services including process_tags."""

from core.models import Tag
from core.services import process_tags

from . import BaseTestCase


class ProcessTagsTest(BaseTestCase):
    """Tests for the process_tags service."""

    def test_process_tags_creates_new_tags(self):
        """Verify that new tags are created and assigned to the post."""
        process_tags(self.post, ["#sunset", "#beach"])

        tag_names = set(self.post.tags.values_list("name", flat=True))

        self.assertEqual(tag_names, {"sunset", "beach"})

    def test_process_tags_strips_hash(self):
        """Verify that leading hash characters are removed."""
        process_tags(self.post, ["#nature"])

        self.assertTrue(
            Tag.objects.filter(name="nature").exists()
        )

    def test_process_tags_lowercases(self):
        """Verify that tags are converted to lowercase."""
        process_tags(self.post, ["#Sunset"])

        self.assertTrue(
            Tag.objects.filter(name="sunset").exists()
        )

    def test_process_tags_reuses_existing(self):
        """Verify that existing tags are reused instead of recreated."""
        Tag.objects.create(name="art")

        process_tags(self.post, ["#art"])

        self.assertEqual(
            Tag.objects.filter(name="art").count(),
            1,
        )
        self.assertIn(
            Tag.objects.get(name="art"),
            self.post.tags.all(),
        )

    def test_process_tags_empty_string_ignored(self):
        """Verify that empty tag values are ignored."""
        process_tags(self.post, ["#", "", "#valid"])

        tag_names = set(self.post.tags.values_list("name", flat=True))

        self.assertEqual(tag_names, {"valid"})

    def test_process_tags_without_hash(self):
        """Verify that tags without a hash are processed correctly."""
        process_tags(self.post, ["travel"])

        self.assertTrue(
            Tag.objects.filter(name="travel").exists()
        )
        self.assertIn(
            Tag.objects.get(name="travel"),
            self.post.tags.all(),
        )
