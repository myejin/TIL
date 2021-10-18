from datetime import datetime
import requests
from pprint import pprint
from config import NAVER

dt = datetime.now()
now = list(datetime.strftime(dt, "%d %b %Y %H").split())
print("now", now)

ID, SECRET = NAVER["ID"], NAVER["PW"]
headers = {"X-Naver-Client-Id": ID, "X-Naver-Client-Secret": SECRET}

query = "삼성전자"
url = f"https://openapi.naver.com/v1/search/news.json?query={query}&display=100"
resp = requests.get(url, headers=headers).json()
items = resp["items"]

url_list = []
for item in items:
    link = item["link"]
    pub_date = list(item["pubDate"].split())
    d, b, Y, H = pub_date[1], pub_date[2], pub_date[3], pub_date[4][:2]
    print(d, b, Y, H)
    if d != now[0]:
        break
    elif b != now[1]:
        break
    elif Y != now[2]:
        break
    elif int(H) < 20 - 1:  # != int(now[3]):
        # 7시 뉴스부터 확인
        break
    url_list.append(link)

print("urls", url_list)
for url in url_list:
    print(url)
print("cnt", len(url_list))
