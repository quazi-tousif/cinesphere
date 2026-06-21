from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True)

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    is_spam = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username
    
    @property
    def followers_count(self):
        return self.follower_relationships.count()


    @property
    def following_count(self):
        return self.following_relationships.count()
    
    def follow(self, user):
        from social.models import Follow

        if self == user:
            return False

        _, created = Follow.objects.get_or_create(
            follower=self,
            following=user,
        )

        return created
    
    def unfollow(self, user):
        from social.models import Follow

        deleted, _ = Follow.objects.filter(
            follower=self,
            following=user,
        ).delete()

        return deleted > 0
    
    def is_following(self, user):
        return self.following_relationships.filter(
            following=user
        ).exists()