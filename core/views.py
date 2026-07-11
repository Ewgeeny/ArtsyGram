from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CategoryFilterForm
from .models import Post



def index(request):
    return HttpResponse("<h1>Welcome to ArtsyGram!</h1>")


def post_list(request):
    posts = Post.objects.all()
    filter_form = CategoryFilterForm(request.GET)

    if filter_form.is_valid():
        category_id = filter_form.cleaned_data["category"]

        if category_id:
            posts = posts.filter(category_id=category_id)

    context = {
        "filter_form": filter_form,
        "posts": posts,
    }

    return render(request, "core/post_list.html", context)


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