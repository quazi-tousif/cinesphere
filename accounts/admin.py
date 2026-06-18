from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "is_staff",
        "is_superuser",
        "is_spam",
        "created_at",
    )

    list_filter = (
        "is_staff",
        "is_superuser",
        "is_spam",
    )

    search_fields = (
        "username",
        "email",
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            "Profile Information",
            {
                "fields": (
                    "bio",
                    "date_of_birth",
                    "profile_picture",
                    "is_spam",
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )