from django.urls import reverse
from movies.models import Movie


def test_movie_list(client, access_db, create_obj):
    url = reverse("movie_list_create")
    resp = client.get(url)
    assert resp.status_code == 200
    assert resp.data[0]["title"] == "해리포터2021"


def test_movie_list_create(client, access_db, create_obj):
    url = reverse("movie_list_create")
    data = {
        "title": "피카츄",
        "overview": "라이츄 꼬부기",
        "release_date": "21-11-08",
        "poster_path": "temp",
        "actor_pks": [1],
    }
    resp = client.post(url, data=data)
    assert resp.status_code == 200
    assert resp.data["title"] == "피카츄"

    obj = Movie.objects.last()
    assert isinstance(obj, Movie)


def test_movie_detail(client, access_db, create_obj):
    url = reverse("movie_detail", kwargs={"movie_pk": 1})
    resp = client.get(url)
    assert resp.status_code == 200
    assert resp.data["title"] == "해리포터2021"

    url = reverse("movie_detail", kwargs={"movie_pk": 2})
    resp = client.get(url)
    assert resp.status_code == 404


def test_review_detail(client, access_db, create_obj):
    url = reverse("review_detail_update_delete", kwargs={"review_pk": 1})
    resp = client.get(url)
    assert resp.status_code == 200
    assert resp.data["title"] == "강추"

    url = reverse("review_detail_update_delete", kwargs={"review_pk": 2})
    resp = client.get(url)
    assert resp.status_code == 404


def test_review_update(client, access_db, create_obj):
    url = reverse("review_detail_update_delete", kwargs={"review_pk": 1})

    resp = client.get(url)
    data = resp.data
    data["title"] = "피카츄2"

    resp = client.put(url, data=data, content_type="application/json")
    assert resp.status_code == 200
    assert resp.data["title"] == "피카츄2"


def test_review_delete(client, access_db, create_obj):
    url = reverse("review_detail_update_delete", kwargs={"review_pk": 1})

    resp = client.delete(url)
    assert resp.status_code == 204
    assert "msg" in resp.data

    resp = client.delete(url)
    assert resp.status_code == 404
