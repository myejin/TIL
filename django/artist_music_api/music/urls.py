from django.urls import path
from . import views

urlpatterns = [
    path("artists/<int:artist_pk>/music/", views.music_create),
    path("music/<int:music_pk>/", views.music_detail_update_delete),
    path("music/", views.music_list),
    path("artists/<int:artist_pk>/", views.artist_detail),
    path("artists/", views.artist_list_create),
]
