import config
import requests
from tmdb import TMDBHelper
from pprint import pprint


def popular_count():
    """
    popular 영화목록의 개수 출력.
    """
    url = TMDBHelper(config.API_KEY).get_request_url()  # 요청1
    results = requests.get(url).json()["results"]  # 요청2
    return len(results)  # 결과


if __name__ == "__main__":
    print(popular_count())
