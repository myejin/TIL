import requests
import os
from dotenv import load_dotenv
load_dotenv()
KEY, TOKEN = os.getenv('DUST_API_KEY'), os.getenv('TELEGRAM_TOKEN')

'''
# 날씨정보
woeid = 1132599
url = f'https://www.metaweather.com/api/location/{woeid}/'
resp = requests.get(url).json() # type(resp): dict
weather = resp["consolidated_weather"][0]["weather_state_name"]
'''

# 미세먼지정보
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=강남구&dataTerm=daily&numOfRows=1&returnType=json&serviceKey={KEY}'
resp = requests.get(url).json()
dust = resp['response']['body']['items'][0]['pm10Value']

msg = f'현재 미세먼지 농도는 {dust}입니다.'
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1818432412&text={msg}'
resp = requests.get(url)
print(resp.status_code)
