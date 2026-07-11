from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="view-index"),
    path("posts/", views.post_list, name="post-list"),
    path(
        "posts/photography/",
        views.photography_posts,
        name="photography-posts",
    ),
    path("home/", views.go_home, name="go-home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)