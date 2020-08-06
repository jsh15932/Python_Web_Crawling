from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text,'html.parser')
html.close()

data1_list = soup.findAll('div',{'class':'col_inner'})

li_list = []
for data1 in data1_list:
    li_list.extend(data1.findAll('li'))

pprint(li_list)