from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path("password/", views.chg_pw, name="chg_pw"),
    path("delete/", views.delete, name="delete"),
    path("update/", views.update, name="update"),
    path("logout/", views.logout, name="logout"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("", views.index, name="index"),
]
