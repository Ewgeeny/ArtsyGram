"""Tests for all application views."""

from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse
from PIL import Image

from core.models import Category, Favorite, Post, Tag

from . import BaseTestCase


def _image_bytes():
    """Return a minimal valid PNG image as bytes."""

    buffer = BytesIO()
    Image.new("RGB", (1, 1), "red").save(buffer, "PNG")
    return buffer.getvalue()


def _upload_image():
    """Return a test image as an uploaded file."""
    return SimpleUploadedFile(
        "test.png",
        _image_bytes(),
        content_type="image/png",
    )


class WelcomeViewTest(TestCase):
    """Tests for the welcome view."""

    def setUp(self):
        """Create a test client and resolve the welcome URL."""
        self.client = Client()
        self.url = reverse("welcome")

    def test_get_anonymous(self):
        """Verify that anonymous users can access the welcome page."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_get_authenticated_redirects(self):
        """Verify that authenticated users are redirected to the main page."""
        User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.client.login(
            username="alice",
            password="pass1234",
        )

        response = self.client.get(self.url)

        self.assertRedirects(response, reverse("main-page"))

    def test_login_valid(self):
        """Verify that a user can log in with valid credentials."""
        User.objects.create_user(
            username="alice",
            password="pass1234",
        )

        response = self.client.post(
            self.url,
            {
                "username": "alice",
                "password": "pass1234",
                "login_submit": "",
            },
        )

        self.assertRedirects(response, reverse("main-page"))

    def test_login_invalid(self):
        """Verify that invalid credentials keep the user on the welcome page."""
        response = self.client.post(
            self.url,
            {
                "username": "noone",
                "password": "bad",
                "login_submit": "",
            },
        )

        self.assertEqual(response.status_code, 200)

    def test_register_valid(self):
        """Verify that a new user can register successfully."""
        response = self.client.post(
            self.url,
            {
                "username": "newuser",
                "password1": "Str0ngP@ss!",
                "password2": "Str0ngP@ss!",
                "register_submit": "",
            },
        )

        self.assertRedirects(response, reverse("main-page"))
        self.assertTrue(
            User.objects.filter(
                username="newuser",
            ).exists()
        )

    def test_register_invalid(self):
        """Verify that invalid registration data is rejected."""
        response = self.client.post(
            self.url,
            {
                "username": "",
                "password1": "foo",
                "password2": "bar",
                "register_submit": "",
            },
        )

        self.assertEqual(response.status_code, 200)


class MainPageViewTest(TestCase):
    """Tests for the main page view."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.client.login(
            username="alice",
            password="pass1234",
        )
        self.url = reverse("main-page")

    def test_get(self):
        """Verify that the main page loads successfully."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_filter_by_category(self):
        """Verify that posts can be filtered by category."""
        other_category = Category.objects.create(name="Photo")

        Post.objects.create(
            user=self.user,
            title="A",
            description="d",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )
        Post.objects.create(
            user=self.user,
            title="B",
            description="d",
            category=other_category,
            upload_date="2026-01-01T00:00:00Z",
        )

        response = self.client.get(
            self.url,
            {"category": self.category.pk},
        )
        posts = response.context["posts"]

        self.assertTrue(
            all(post.category == self.category for post in posts)
        )

    def test_filter_by_tag(self):
        """Verify that posts can be filtered by tag."""
        tag = Tag.objects.create(name="sunset")
        post = Post.objects.create(
            user=self.user,
            title="Sunset",
            description="d",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )
        post.tags.add(tag)

        response = self.client.get(
            self.url,
            {"tags": "sunset"},
        )

        self.assertIn(post, response.context["posts"])

    def test_unauthenticated_redirect(self):
        """Verify that anonymous users are redirected to the welcome page."""
        self.client.logout()

        response = self.client.get(self.url)

        self.assertRedirects(
            response,
            f"{reverse('welcome')}?next={self.url}",
        )


class UserProfileViewTest(TestCase):
    """Tests for the user profile view."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.other = User.objects.create_user(
            username="bob",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.client.login(
            username="alice",
            password="pass1234",
        )

    def test_own_profile(self):
        """Verify that users can view their own profile."""
        response = self.client.get(
            reverse(
                "user-profile",
                args=["alice"],
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["is_own_profile"])

    def test_other_profile(self):
        """Verify that users can view another user's profile."""
        response = self.client.get(
            reverse(
                "user-profile",
                args=["bob"],
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context["is_own_profile"])

    def test_nonexistent_user(self):
        """Verify that requesting an unknown user returns 404."""
        response = self.client.get(
            reverse(
                "user-profile",
                args=["nobody"],
            )
        )

        self.assertEqual(response.status_code, 404)


class UserFavoritesViewTest(TestCase):
    """Tests for the user favorites view."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.other = User.objects.create_user(
            username="bob",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.client.login(
            username="alice",
            password="pass1234",
        )

    def test_own_favorites(self):
        """Verify that users can view their own favorites."""
        response = self.client.get(
            reverse(
                "user-favorites",
                args=["alice"],
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_other_user_favorites_forbidden(self):
        """Verify that users cannot access another user's favorites."""
        response = self.client.get(
            reverse(
                "user-favorites",
                args=["bob"],
            )
        )

        self.assertEqual(response.status_code, 403)


class CreatePostViewTest(TestCase):
    """Tests for the create post view."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.client.login(
            username="alice",
            password="pass1234",
        )
        self.url = reverse("create-post")

    def test_get(self):
        """Verify that the create post page loads successfully."""
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_post_valid(self):
        """Verify that a valid post is created successfully."""
        response = self.client.post(
            self.url,
            {
                "title": "My Art",
                "image": _upload_image(),
                "description": "Beautiful",
                "category": self.category.pk,
                "tags": "#art #cool",
            },
            format="multipart",
        )

        self.assertRedirects(
            response,
            reverse(
                "user-profile",
                args=["alice"],
            ),
        )
        self.assertEqual(Post.objects.count(), 1)

        post = Post.objects.first()

        self.assertEqual(
            set(post.tags.values_list("name", flat=True)),
            {"art", "cool"},
        )

    def test_post_invalid(self):
        """Verify that invalid post data is rejected."""
        response = self.client.post(
            self.url,
            {"title": ""},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), 0)


class DeletePostViewTest(TestCase):
    """Tests for the delete post view."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.other = User.objects.create_user(
            username="bob",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.client.login(
            username="alice",
            password="pass1234",
        )
        self.post = Post.objects.create(
            user=self.user,
            title="Mine",
            description="d",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

    def test_delete_own_post(self):
        """Verify that users can delete their own posts."""
        response = self.client.post(
            reverse(
                "delete-post",
                args=[self.post.pk],
            )
        )

        self.assertRedirects(
            response,
            reverse(
                "user-profile",
                args=["alice"],
            ),
        )
        self.assertFalse(
            Post.objects.filter(
                pk=self.post.pk,
            ).exists()
        )

    def test_delete_other_post_noop(self):
        """Verify that users cannot delete another user's post."""
        other_post = Post.objects.create(
            user=self.other,
            title="Bobs",
            description="d",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

        self.client.post(
            reverse(
                "delete-post",
                args=[other_post.pk],
            )
        )

        self.assertTrue(
            Post.objects.filter(
                pk=other_post.pk,
            ).exists()
        )

    def test_delete_post_get_redirects(self):
        """Verify that a GET request does not delete a post."""
        response = self.client.get(
            reverse(
                "delete-post",
                args=[self.post.pk],
            )
        )

        self.assertRedirects(
            response,
            reverse(
                "user-profile",
                args=["alice"],
            ),
        )


class EditPostViewTest(TestCase):
    """Tests for the edit post view."""

    def setUp(self):
        """Create shared test data."""
        self.user = User.objects.create_user(
            username="alice",
            password="pass1234",
        )
        self.other = User.objects.create_user(
            username="bob",
            password="pass1234",
        )
        self.category = Category.objects.create(name="Art")
        self.client.login(
            username="alice",
            password="pass1234",
        )
        self.post = Post.objects.create(
            user=self.user,
            title="Old Title",
            description="Old desc",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

    def test_get_edit_form(self):
        """Verify that the edit form contains the existing post data."""
        response = self.client.get(
            reverse(
                "edit-post",
                args=[self.post.pk],
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["form"].initial["title"],
            "Old Title",
        )

    def test_post_valid_update(self):
        """Verify that a post is updated with valid data."""
        response = self.client.post(
            reverse(
                "edit-post",
                args=[self.post.pk],
            ),
            {
                "title": "New Title",
                "description": "New desc",
                "category": self.category.pk,
                "tags": "#updated",
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "user-profile",
                args=["alice"],
            ),
        )

        self.post.refresh_from_db()

        self.assertEqual(self.post.title, "New Title")
        self.assertEqual(
            set(self.post.tags.values_list("name", flat=True)),
            {"updated"},
        )

    def test_edit_other_post_redirects(self):
        """Verify that users cannot edit another user's post."""
        other_post = Post.objects.create(
            user=self.other,
            title="Bobs",
            description="d",
            category=self.category,
            upload_date="2026-01-01T00:00:00Z",
        )

        response = self.client.get(
            reverse(
                "edit-post",
                args=[other_post.pk],
            )
        )

        self.assertRedirects(
            response,
            reverse(
                "user-profile",
                args=["alice"],
            ),
        )

    def test_post_invalid(self):
        """Verify that invalid post updates are rejected."""
        response = self.client.post(
            reverse(
                "edit-post",
                args=[self.post.pk],
            ),
            {"title": ""},
        )

        self.assertEqual(response.status_code, 200)


class ToggleFavoriteViewTest(BaseTestCase):
    """Tests for the toggle favorite view."""

    def setUp(self):
        """Create shared test data and log in."""
        super().setUp()
        self.client.login(
            username="alice",
            password="pass1234",
        )
        self.url = reverse(
            "toggle-favorite",
            args=[self.post.pk],
        )

    def test_toggle_add(self):
        """Verify that toggling adds a post to the user's favorites."""
        response = self.client.post(self.url)

        self.assertRedirects(response, reverse("main-page"))
        self.assertTrue(self._favorite_exists())

    def test_toggle_remove(self):
        """Verify that toggling removes an existing favorite."""
        Favorite.objects.create(
            user=self.user,
            post=self.post,
        )

        response = self.client.post(self.url)

        self.assertRedirects(response, reverse("main-page"))
        self.assertFalse(self._favorite_exists())

    def test_toggle_nonexistent_post(self):
        """Verify that toggling an unknown post is handled safely."""
        response = self.client.post(
            reverse(
                "toggle-favorite",
                args=[9999],
            )
        )

        self.assertRedirects(response, reverse("main-page"))

    def test_hx_request_from_main(self):
        """Verify the HTMX response from the main page."""
        response = self.client.post(
            self.url,
            HTTP_HX_REQUEST="true",
        )

        self.assertEqual(response.status_code, 200)

    def test_hx_request_from_favorites_page(self):
        """Verify the HTMX response from the favorites page."""
        Favorite.objects.create(
            user=self.user,
            post=self.post,
        )

        response = self.client.post(
            self.url,
            {"from_favorites": "true"},
            HTTP_HX_REQUEST="true",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"")

    def test_get_redirects(self):
        """Verify that GET requests are redirected to the main page."""
        response = self.client.get(self.url)

        self.assertRedirects(response, reverse("main-page"))


class UnauthenticatedAccessTest(BaseTestCase):
    """Tests for views that require authentication."""

    def test_create_post_requires_login(self):
        """Verify that creating posts requires authentication."""
        response = self.client.get(reverse("create-post"))

        self.assertRedirects(
            response,
            f"{reverse('welcome')}?next={reverse('create-post')}",
        )

    def test_edit_post_requires_login(self):
        """Verify that editing posts requires authentication."""
        edit_url = reverse(
            "edit-post",
            args=[self.post.pk],
        )

        response = self.client.get(edit_url)

        self.assertRedirects(
            response,
            f"{reverse('welcome')}?next={edit_url}",
        )

    def test_delete_post_requires_login(self):
        """Verify that deleting posts requires authentication."""
        delete_url = reverse(
            "delete-post",
            args=[self.post.pk],
        )

        response = self.client.post(delete_url)

        self.assertRedirects(
            response,
            f"{reverse('welcome')}?next={delete_url}",
        )

    def test_toggle_favorite_requires_login(self):
        """Verify that toggling favorites requires authentication."""
        favorite_url = reverse(
            "toggle-favorite",
            args=[self.post.pk],
        )

        response = self.client.post(favorite_url)

        self.assertRedirects(
            response,
            f"{reverse('welcome')}?next={favorite_url}",
        )


class MainPageFavoriteIdsTest(BaseTestCase):
    """Tests for favorite IDs in the main page context."""

    def setUp(self):
        """Create shared test data and log in."""
        super().setUp()
        self.client.login(
            username="alice",
            password="pass1234",
        )

    def test_favorite_ids_in_context(self):
        """Verify that favorite post IDs are included in the context."""
        response = self.client.get(reverse("main-page"))

        self.assertNotIn(
            self.post.pk,
            response.context["favorite_ids"],
        )

        Favorite.objects.create(
            user=self.user,
            post=self.post,
        )

        response = self.client.get(reverse("main-page"))

        self.assertIn(
            self.post.pk,
            response.context["favorite_ids"],
        )
