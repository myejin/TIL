from rest_framework import serializers
from ..models import Actor, Review, Movie


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            "id",
            "title",
        )


class ReviewSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = (
                "id",
                "title",
            )

    movie = MovieListSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
