from rest_framework import serializers
from ..models import Actor, Review, Movie


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
        )


class MovieSerializer(serializers.ModelSerializer):
    class ActorListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Actor
            fields = "__all__"

    class ReviewListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = (
                "id",
                "title",
            )

    actors = ActorListSerializer(many=True, read_only=True)
    reviews = ReviewListSerializer(many=True, read_only=True)

    actor_pks = serializers.ListField(write_only=True)

    def create(self, validated_data):
        actor_pks = validated_data.pop("actor_pks")
        movie = Movie.objects.create(**validated_data)

        for actor_pk in actor_pks:
            movie.actors.add(actor_pk)

        return movie

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "overview",
            "poster_path",
            "actors",
            "reviews",
            "actor_pks",
        )
