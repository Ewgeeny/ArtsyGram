## Context

The app currently has collection functionality that does not match the desired user flow. A private favorites list is needed instead, displayed on the profile sorted by save time.

## Goals / Non-Goals

**Goals:**
- Enable saving and removing posts as favorites.
- Provide a private profile view showing only own favorites.
- Sort favorites by save time, most recently saved first.
- Cleanly remove existing collection functionality from UI and logic.

**Non-Goals:**
- No public collections or sharing features for favorites.
- No separate folders/tags within favorites.
- No restoration of old collection data unless explicitly requested.

## Decisions

- New `Favorite` model with `user`, `post`, and `saved_at` instead of generic collection structure.
- Unique constraint `unique_together` on user/post to prevent duplicates.
- Favorites toggleable via POST endpoints, profile view via GET.
- Sorting in profile view via `-saved_at` to show newest entries first.
- Collection model, admin entry, and related views are removed.

## Risks / Trade-offs

- [Data loss of old collections] → Check migration; if no user data is relevant, document clearly.
- [Confusion from feature switch] → Use UI hints for favorites instead of collections.
- [Double clicks/status] → Secure toggle logic with uniqueness constraint.
