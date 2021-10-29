from rest_framework import serializers
from ..models import Actor, Review, Movie


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "id",
                "title",
            )

    movies = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = "__all__"
