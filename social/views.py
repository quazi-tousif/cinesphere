from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReviewForm
from .models import Movie, Review

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "social/movie_list.html", {"movies": movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    reviews = Review.objects.filter(movie=movie).select_related("user")

    if request.method == "POST" and request.user.is_authenticated:
        form = ReviewForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            Review.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={
                    "rating": review.rating,
                    "review_text": review.review_text,
                    },
                )

            return redirect("social:movie_detail", movie_id=movie.id)
    else:
        form = ReviewForm()

    context = {
        "movie": movie,
        "reviews": reviews,
        "form": form,
    }

    return render(request, "social/movie_detail.html", context)