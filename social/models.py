from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError

class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following_relationships",
    )

    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="follower_relationships",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="unique_follow_relationship",
            )
        ]
        ordering = ["-created_at"]

    def clean(self):
        if self.follower == self.following:
            raise ValidationError("Users cannot follow themselves.")

    def __str__(self):
        return f"{self.follower} follows {self.following}"
    
class Movie(models.Model):
    title = models.CharField(max_length=255)

    release_year = models.PositiveIntegerField()

    description = models.TextField(blank=True)

    runtime = models.PositiveIntegerField(
        help_text="Runtime in minutes"
    )

    language = models.CharField(
        max_length=50,
        default="English"
    )

    genre = models.CharField(
        max_length=100,
        default="Unknown",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title
    
class Review(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField()

    review_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_user_movie_review",
            )
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user} reviewed {self.movie}"