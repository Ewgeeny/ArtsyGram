from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Post


def index(request):
    return HttpResponse("<h1>Welcome to ArtsyGram!</h1>")


def post_list(request):
    posts = Post.objects.all()

    result = "<h1>All Posts</h1>"

    for post in posts:
        result += f"<p>{post.title}</p>"

    return HttpResponse(result)


def photography_posts(request):
    posts = Post.objects.filter(
        category__name="Photography"
    ).order_by("-upload_date")

    result = "<h1>Photography Posts</h1>"

    for post in posts:
        result += f"<p>{post.title}</p>"

    return HttpResponse(result)


def go_home(request):
    return redirect("view-index")