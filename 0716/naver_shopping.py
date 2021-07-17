import requests
from pprint import pprint # pretty print 
import os
from dotenv import load_dotenv
load_dotenv()
ID, SECRET, TOKEN = os.getenv('NAVER_ID'), os.getenv('NAVER_SECRET'), os.getenv('NAVER_BOT')

headers = {
    'X-Naver-Client-Id': ID,
    'X-Naver-Client-Secret': SECRET
}
query = '닌텐도'
url = f'https://openapi.naver.com/v1/search/shop.json?query={query}'
resp = requests.get(url, headers=headers).json()
#pprint(resp)

min_price = float('inf')
object = {}
for item in resp['items']:
    lprice = int(item['lprice'])
    if lprice < min_price:
        min_price = lprice
        object = item

msg = f'- 최저가명: {object["title"]}\n- 최저가: {min_price}원\n- 링크: {object["link"]} '
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1818432412&text={msg}'
resp = requests.get(url)
print(resp.status_code)
