import config
import requests
from tmdb import TMDBHelper
from pprint import pprint


def vote_average_movies():
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    movie_list = []
    url = TMDBHelper(config.API_KEY).get_request_url()  # 요청1
    results = requests.get(url).json()["results"]  # 요청2
    for movie in results:
        if movie["vote_average"] >= 8:
            movie_list.append(movie)
    return movie_list  # 결과


if __name__ == "__main__":
    pprint(vote_average_movies())
