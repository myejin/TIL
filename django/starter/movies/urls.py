from . import views
from django.urls import path

app_name = "movies"
urlpatterns = [
    path("new/", views.new, name="new"),
    path("create/", views.create, name="create"),
    path("", views.index, name="index"),
    path("<pk>/", views.detail, name="detail"),
    path("<pk>/edit/", views.edit, name="edit"),
    path("<pk>/update/", views.update, name="update"),
    path("<pk>/delete/", views.delete, name="delete"),
]
