import pytest
from movies.models import Actor, Movie, Review


@pytest.fixture
def access_db(db):  # 이미 존재하는 가? 따로 정의 필요없는가?
    pass


@pytest.fixture(scope="module")
def create_obj(django_db_blocker):
    with django_db_blocker.unblock():
        actor = Actor.objects.create(name="Hyejin")
        movie = Movie.objects.create(
            title="해리포터2021",
            overview="해리와 헤르미온느와 론",
            release_date="21-11-08",
            poster_path="temp",
        )
        movie.actors.add(actor)
        Review.objects.create(
            title="강추",
            content="너무 재밌었네요",
            rank="5",
            movie=movie,
        )
    # 장고는 끝맺는거 없나?
