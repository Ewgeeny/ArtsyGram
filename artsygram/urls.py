from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from core import views


urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        views.welcome,
        name="welcome",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
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
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)