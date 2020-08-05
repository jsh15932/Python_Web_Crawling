from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('http://comic.naver.com/webtoon/weekday.nhn')
soup = bs(html.text,'html.parser')
html.close()

data1 = soup.find('div',{'class':'col_inner'})
# pprint(data1)

data2 = data1.findAll('a',{'class':'title'})

title_list = [t.text for t in data2]

pprint(title_list)