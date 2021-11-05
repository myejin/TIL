from django.core import paginator
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.views.decorators.http import require_safe
from django.core.paginator import Paginator
from django.core import serializers
from .models import Movie, Genre
import random


@require_safe
def index(request):
    movies = get_list_or_404(Movie)
    paginator = Paginator(movies, 10)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        data = serializers.serialize("json", page_obj)
        return HttpResponse(data, content_type="application/json")
    else:
        context = {
            "movies": page_obj,
            "movies_cnt": len(movies),
        }
        return render(request, "movies/index.html", context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    genres = [genre.name for genre in movie.genres.all()]

    context = {
        "movie": movie,
        "genres": genres,
    }
    return render(request, "movies/detail.html", context)


@require_safe
def recommended(request):
    movies = get_list_or_404(Movie)
    recommended_movies = random.sample(movies, 10)
    
    context = {
        'recommended_movies': recommended_movies,
    }
    return render(request, "movies/recommended.html", context)