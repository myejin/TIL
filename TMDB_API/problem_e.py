import config
import requests
from tmdb import TMDBHelper
from pprint import pprint


def credits(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록과 목록을 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    helper = TMDBHelper(config.API_KEY)
    movie_id = helper.get_movie_id(title)  # 요청1
    if movie_id is None:
        return None

    method = f"/movie/{movie_id}/credits"
    url = helper.get_request_url(method)  # 요청2
    data = requests.get(url).json()  # 요청3

    actors = []
    for actor in data["cast"]:
        if actor["cast_id"] < 10:
            actors.append(actor["name"])  # 결과1

    director = []
    for crew in data["crew"]:
        if crew["department"] == "Directing":
            director.append(crew["name"])  # 결과2

    return {"cast": actors, "crew": director}  # 결과3, 4


if __name__ == "__main__":
    pprint(credits("기생충"))
    pprint(credits("검색할 수 없는 영화"))
