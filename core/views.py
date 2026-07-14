from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CategoryFilterForm, PostForm
from .models import Post


def welcome(request):
    if request.user.is_authenticated:
        return redirect("main-page")

    login_form = AuthenticationForm(request)
    register_form = UserCreationForm()

    if request.method == "POST":
        if "login_submit" in request.POST:
            login_form = AuthenticationForm(
                request,
                data=request.POST,
            )

            if login_form.is_valid():
                login(request, login_form.get_user())
                return redirect("main-page")

        elif "register_submit" in request.POST:
            register_form = UserCreationForm(request.POST)

            if register_form.is_valid():
                new_user = register_form.save()
                login(request, new_user)
                return redirect("main-page")

    context = {
        "login_form": login_form,
        "register_form": register_form,
    }

    return render(request, "core/welcome.html", context)


@login_required
def main_page(request):
    posts = Post.objects.order_by("-upload_date")
    filter_form = CategoryFilterForm(request.GET)

    if filter_form.is_valid():
        category = filter_form.cleaned_data["category"]

        if category:
            posts = posts.filter(category=category)

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

    posts = Post.objects.filter(
        user=profile_user
    ).order_by("-upload_date")

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
            Post.objects.create(
                user=request.user,
                title=form.cleaned_data["title"],
                image=request.FILES["image"],
                description=form.cleaned_data["description"],
                category=form.cleaned_data["category"],
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