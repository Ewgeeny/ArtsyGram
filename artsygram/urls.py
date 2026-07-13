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
        auth_views.LoginView.as_view(
            template_name="core/welcome.html",
            redirect_authenticated_user=True,
        ),
        name="login",
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
        "posts/create/",
        views.create_post,
        name="create-post",
    ),
    path(
        "posts/<int:post_id>/delete/",
        views.delete_post,
        name="delete-post",
    ),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)

