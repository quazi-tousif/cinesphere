from django.urls import path

from .views import movie_detail, movie_list

app_name = "social"

urlpatterns = [
    path("", movie_list, name="movie_list"),
    path("<int:movie_id>/", movie_detail, name="movie_detail"),
]