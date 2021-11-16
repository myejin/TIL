from django.urls import path
from . import views


urlpatterns = [
    path("actors/", views.actor_list),
    path("actors/<int:actor_pk>/", views.actor_detail),
    path("movies/", views.movie_list_create, name="movie_list_create"),
    path("movies/<int:movie_pk>/", views.movie_detail, name="movie_detail"),
    path("reviews/", views.review_list),
    path(
        "reviews/<int:review_pk>/",
        views.review_detail_update_delete,
        name="review_detail_update_delete",
    ),
    path("movies/<int:movie_pk>/reviews/", views.review_create),
]
