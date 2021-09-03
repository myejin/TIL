import movies
from django.shortcuts import redirect, render
from .models import Movie

# Create your views here.
def new(request):
    return render(request, "movies/new.html")


def create(request):
    title = request.POST.get("title")
    overview = request.POST.get("overview")
    poster_path = request.POST.get("poster_path")
    movies = Movie()
    movies.title = title
    movies.overview = overview
    movies.poster_path = poster_path
    movies.save()
    return redirect("movies:index")


def index(request):
    movies = Movie.objects.all()
    context = {"movies": movies}
    return render(request, "movies/index.html", context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {"movie": movie}
    return render(request, "movies/detail.html", context)


def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {"movie": movie}
    return render(request, "movies/edit.html", context)


def update(request, pk):
    title = request.POST.get("title")
    overview = request.POST.get("overview")
    poster_path = request.POST.get("poster_path")
    movie = Movie.objects.get(pk=pk)
    movie.title = title
    movie.overview = overview
    movie.poster_path = poster_path
    movie.save()
    return redirect("movies:detail", movie.pk)


def delete(request, pk):
    if request.method == "POST":
        movie = Movie.objects.get(pk=pk)
        movie.delete()
    return redirect("movies:index")
