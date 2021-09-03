from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")


admin.site.register(Movie)
