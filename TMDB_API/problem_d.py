import config
import requests
from tmdb import TMDBHelper
from pprint import pprint


def recommendation(title):
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록을 출력.
    추천 영화가 없을 경우 [] 출력.
    영화 id검색에 실패할 경우 None 출력.
    """
    helper = TMDBHelper(config.API_KEY)
    movie_id = helper.get_movie_id(title)  # 요청1
    if movie_id is None:
        return None  # 결과3

    method = f"/movie/{movie_id}/recommendations"
    url = helper.get_request_url(method, language="ko")  # 요청2
    results = requests.get(url).json()["results"]  # 요청3
    if not results:
        return []  # 결과4

    movie_list = []
    for movie in results:
        title = movie["title"]
        movie_list.append(title)  # 결과1
    return movie_list  # 결과2


if __name__ == "__main__":
    pprint(recommendation("기생충"))
    pprint(recommendation("그래비티"))
    pprint(recommendation("검색할 수 없는 영화"))
