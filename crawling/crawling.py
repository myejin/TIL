import requests
from bs4 import BeautifulSoup # beautifulsoup4

resp = requests.get('https://finance.naver.com/sise/').text
html = BeautifulSoup(resp, 'html.parser')
kospi = html.select_one('#KOSPI_now').text
print(kospi)
