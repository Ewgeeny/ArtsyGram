from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import CategoryFilterForm, EditPostForm, PostForm
from .models import Category, Favorite, Post, Tag
from .services import toggle_favorite


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
    categories = Category.objects.all()

    category_id = request.GET.get("category")
    if category_id:
        posts = posts.filter(category_id=category_id)

    if filter_form.is_valid():
        tags_input = filter_form.cleaned_data["tags"]

        if tags_input:
            posts = posts.filter(tags__name=tags_input)

    favorite_ids = Favorite.objects.filter(
        user=request.user
    ).values_list("post_id", flat=True)

    context = {
        "posts": posts,
        "filter_form": filter_form,
        "categories": categories,
        "selected_category": category_id,
        "favorite_ids": favorite_ids,
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
def user_favorites(request, username):
    users = User.objects.filter(username=username)

    if len(users) == 0:
        return HttpResponse("User not found.", status=404)

    profile_user = users[0]

    if request.user != profile_user:
        return HttpResponse("Not authorized.", status=403)

    favorites = Favorite.objects.filter(
        user=request.user
    ).select_related("post").order_by("-saved_at")

    context = {
        "profile_user": profile_user,
        "favorites": favorites,
    }

    return render(request, "core/favorites.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post.objects.create(
                user=request.user,
                title=form.cleaned_data["title"],
                image=request.FILES["image"],
                description=form.cleaned_data["description"],
                category=form.cleaned_data["category"],
                upload_date=timezone.now(),
            )

            tags = form.cleaned_data["tags"].split()

            for tag in tags:
                tag_name = tag.lstrip("#").lower()

                if tag_name:
                    existing_tags = Tag.objects.filter(name=tag_name)

                    if len(existing_tags) == 0:
                        tag = Tag.objects.create(name=tag_name)
                    else:
                        tag = existing_tags[0]

                    post.tags.add(tag)

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


@login_required
def edit_post(request, post_id):
    posts = Post.objects.filter(id=post_id, user=request.user)

    if not posts.exists():
        return redirect("user-profile", username=request.user.username)

    post = posts[0]

    if request.method == "POST":
        form = EditPostForm(request.POST)

        if form.is_valid():
            post.title = form.cleaned_data["title"]
            post.description = form.cleaned_data["description"]
            post.category = form.cleaned_data["category"]
            post.save()

            post.tags.clear()

            tags = form.cleaned_data["tags"].split()

            for tag in tags:
                tag_name = tag.lstrip("#").lower()

                if tag_name:
                    existing_tags = Tag.objects.filter(name=tag_name)

                    if len(existing_tags) == 0:
                        tag = Tag.objects.create(name=tag_name)
                    else:
                        tag = existing_tags[0]

                    post.tags.add(tag)

            return redirect(
                "user-profile",
                username=request.user.username,
            )
    else:
        form = EditPostForm(
            initial={
                "title": post.title,
                "description": post.description,
                "category": post.category,
                "tags": " ".join(
                    [f"#{t.name}" for t in post.tags.all()]
                ),
            }
        )

    return render(
        request,
        "core/edit_post.html",
        {"form": form, "post": post},
    )


@login_required
def toggle_favorite_view(request, post_id):
    if request.method == "POST":
        post = Post.objects.filter(id=post_id).first()

        if post:
            toggle_favorite(request.user, post)

            if request.headers.get("HX-Request"):
                if "favorites" in request.path:
                    return HttpResponse("")

                favorite_ids = Favorite.objects.filter(
                    user=request.user
                ).values_list("post_id", flat=True)

                return render(
                    request,
                    "core/favorite_button.html",
                    {"post": post, "favorite_ids": favorite_ids},
                )

    referer = request.META.get("HTTP_REFERER")
    if referer:
        return redirect(referer)
    return redirect("main-page")