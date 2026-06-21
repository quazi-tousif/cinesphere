from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User


def profile_view(request, username):
    user = get_object_or_404(User, username=username)

    is_following = False

    if request.user.is_authenticated:
        is_following = request.user.is_following(user)

    return render(
        request,
        "accounts/profile.html",
        {
            "profile_user": user,
            "is_following": is_following,
        },
    )

@login_required
def follow_toggle(request, username):
    target = get_object_or_404(User, username=username)

    if request.user == target:
        return redirect("accounts:profile", username=username)

    if request.user.is_following(target):
        request.user.unfollow(target)
    else:
        request.user.follow(target)

    return redirect("accounts:profile", username=username)