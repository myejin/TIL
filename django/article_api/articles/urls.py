from django.urls import path
from . import views

urlpatterns = [
    path("article/<int:article_pk>/", views.article_detail_update_delete),
    path("articles/", views.article_list_create),
]
