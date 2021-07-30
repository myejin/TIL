import config
import requests
from tmdb import TMDBHelper
from pprint import pprint


def ranking():
    """
    popular 영화목록을 정렬하여 평점순으로 5개 출력.
    """
    movie_list = []
    url = TMDBHelper(config.API_KEY).get_request_url()  # 요청1
    results = requests.get(url).json()["results"]  # 요청2
    for idx, movie in enumerate(results):
        movie_list.append([movie["vote_average"], idx])
    movie_list.sort(reverse=True)  # 평점(과 인덱스) 기준으로 내림차순 정렬

    ret = []
    for i in range(5):  # 다섯 개 반환 예정
        idx = movie_list[i][1]  # 평점 높은 영화의 인덱스
        ret.append(results[idx])  # 해당 인덱스의 영화
    return ret


if __name__ == "__main__":
    pprint(ranking())
