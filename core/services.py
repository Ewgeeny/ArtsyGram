from .models import Favorite


def toggle_favorite(user, post):
    favorite = Favorite.objects.filter(user=user, post=post)

    if favorite.exists():
        favorite.delete()
        return False
    else:
        Favorite.objects.create(user=user, post=post)
        return True
