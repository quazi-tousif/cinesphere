from django.contrib import admin

from .models import Follow, Movie, Review


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("follower", "following", "created_at")
    search_fields = ("follower__username", "following__username")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_year",
        "runtime",
        "language",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
    )

    list_filter = (
        "release_year",
        "language",
    )

    ordering = (
        "title",
    )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "movie",
        "rating",
        "created_at",
    )

    search_fields = (
        "user__username",
        "movie__title",
    )

    list_filter = (
        "rating",
        "created_at",
    )

    ordering = (
        "-created_at",
    )