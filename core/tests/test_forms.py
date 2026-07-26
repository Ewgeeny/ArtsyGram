"""Tests for forms."""

from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from PIL import Image

from core.forms import CategoryFilterForm, EditPostForm, PostForm
from core.models import Category


class CategoryFilterFormTest(TestCase):
    """Tests for the category and tag filter form."""

    def test_valid_single_tag(self):
        """Verify that a single tag is accepted."""
        form = CategoryFilterForm(data={"tags": "sunset"})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["tags"], "sunset")

    def test_strips_hash_prefix(self):
        """Verify that a leading hash character is removed."""
        form = CategoryFilterForm(data={"tags": "#sunset"})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["tags"], "sunset")

    def test_lowercases_tag(self):
        """Verify that tags are converted to lowercase."""
        form = CategoryFilterForm(data={"tags": "Sunset"})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["tags"], "sunset")

    def test_empty_tag_valid(self):
        """Verify that an empty tag value is accepted."""
        form = CategoryFilterForm(data={"tags": ""})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["tags"], "")

    def test_spaces_rejected(self):
        """Verify that multiple space-separated tags are rejected."""
        form = CategoryFilterForm(data={"tags": "one two"})

        self.assertFalse(form.is_valid())
        self.assertIn("tags", form.errors)

    def test_strips_whitespace(self):
        """Verify that surrounding whitespace is removed."""
        form = CategoryFilterForm(data={"tags": "  sunset  "})

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["tags"], "sunset")


class PostFormTest(TestCase):
    """Tests for the post creation form."""

    def setUp(self):
        """Create a category used by the form tests."""
        self.category = Category.objects.create(name="Art")

    def test_valid_data(self):
        """Verify that valid post data and an image are accepted."""
        buffer = BytesIO()
        Image.new("RGB", (1, 1), "red").save(buffer, "PNG")

        image = SimpleUploadedFile(
            "test.png",
            buffer.getvalue(),
            content_type="image/png",
        )

        form = PostForm(
            data={
                "title": "My Post",
                "description": "Nice pic",
                "category": self.category.pk,
                "tags": "#art #painting",
            },
            files={"image": image},
        )

        self.assertTrue(form.is_valid())

    def test_missing_title(self):
        """Verify that the title field is required."""
        form = PostForm(
            data={
                "title": "",
                "description": "Nice pic",
                "category": self.category.pk,
                "tags": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_missing_category(self):
        """Verify that the category field is required."""
        form = PostForm(
            data={
                "title": "My Post",
                "description": "Nice pic",
                "category": "",
                "tags": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("category", form.errors)


class EditPostFormTest(TestCase):
    """Tests for the post editing form."""

    def setUp(self):
        """Create a category used by the form tests."""
        self.category = Category.objects.create(name="Art")

    def test_valid_data_without_image(self):
        """Verify that a post can be edited without uploading an image."""
        form = EditPostForm(
            data={
                "title": "Updated Title",
                "description": "Updated desc",
                "category": self.category.pk,
                "tags": "#newtag",
            }
        )

        self.assertTrue(form.is_valid())

    def test_no_image_field(self):
        """Verify that the edit form does not contain an image field."""
        form = EditPostForm()

        self.assertNotIn("image", form.fields)
