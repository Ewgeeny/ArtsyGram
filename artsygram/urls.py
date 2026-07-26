"""URL configuration for the ArtsyGram project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from core import views


class PostOnlyLogoutView(auth_views.LogoutView):
    """Logout view that only accepts POST requests."""

    http_method_names = ["post"]


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "",
        views.welcome,
        name="welcome",
    ),
    path(
        "logout/",
        PostOnlyLogoutView.as_view(),
        name="logout",
    ),
    path(
        "main/",
        views.main_page,
        name="main-page",
    ),
    path(
        "profile/<str:username>/",
        views.user_profile,
        name="user-profile",
    ),
    path(
        "profile/<str:username>/favorites/",
        views.user_favorites,
        name="user-favorites",
    ),
    path(
        "posts/create/",
        views.create_post,
        name="create-post",
    ),
    path(
        "posts/<int:post_id>/delete/",
        views.delete_post,
        name="delete-post",
    ),
    path(
        "posts/<int:post_id>/edit/",
        views.edit_post,
        name="edit-post",
    ),
    path(
        "posts/<int:post_id>/favorite/",
        views.toggle_favorite_view,
        name="toggle-favorite",
    ),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
