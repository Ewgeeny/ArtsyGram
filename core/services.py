"""Service functions for post and favorite management."""

from .models import Favorite, Tag


def toggle_favorite(user, post):
    """Add or remove a post from a user's favorites."""
    favorite = Favorite.objects.filter(user=user, post=post)

    if favorite.exists():
        favorite.delete()
        return False

    Favorite.objects.create(user=user, post=post)
    return True


def process_tags(post, tags):
    """Create missing tags and assign them to a post."""
    for tag in tags:
        tag_name = tag.lstrip("#").lower()

        if tag_name:
            tag_obj, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag_obj)
