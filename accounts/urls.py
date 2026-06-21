from django.urls import path

from .views import profile_view, follow_toggle

app_name = "accounts"

urlpatterns = [
    path("<str:username>/", profile_view, name="profile"),
    path("<str:username>/follow/", follow_toggle, name="follow_toggle"),
]