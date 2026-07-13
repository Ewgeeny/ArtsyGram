from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CategoryFilterForm, PostForm
from .models import Category, Post


@login_required
def main_page(request):
    posts = Post.objects.order_by("-upload_date")
    filter_form = CategoryFilterForm(request.GET)

    if filter_form.is_valid():
        category_name = filter_form.cleaned_data["category"]

        if category_name:
            posts = posts.filter(category__name=category_name)

    context = {
        "posts": posts,
        "filter_form": filter_form,
    }

    return render(request, "core/main_page.html", context)


@login_required
def user_profile(request, username):
    users = User.objects.filter(username=username)

    if len(users) == 0:
        return HttpResponse("User not found.", status=404)

    profile_user = users[0]
    posts = Post.objects.filter(user=profile_user).order_by("-upload_date")

    context = {
        "profile_user": profile_user,
        "posts": posts,
        "is_own_profile": request.user == profile_user,
    }

    return render(request, "core/user_profile.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            category = Category.objects.filter(name=form.cleaned_data["category"]).get()

            Post.objects.create(
                user=request.user,
                title=form.cleaned_data["title"],
                image=request.FILES["image"],
                description=form.cleaned_data["description"],
                category=category,
                upload_date=timezone.now(),
            )

            return redirect(
                "user-profile",
                username=request.user.username,
            )
    else:
        form = PostForm()

    return render(
        request,
        "core/create_post.html",
        {"form": form},
    )


@login_required
def delete_post(request, post_id):
    if request.method == "POST":
        posts = Post.objects.filter(
            id=post_id,
            user=request.user,
        )

        if len(posts) > 0:
            posts[0].delete()

    return redirect(
        "user-profile",
        username=request.user.username,
    )
