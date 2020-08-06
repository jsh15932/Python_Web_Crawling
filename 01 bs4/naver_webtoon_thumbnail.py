from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html,'html.parser')
html.close()

data1 = soup.findAll('a',{'class':'title'})
