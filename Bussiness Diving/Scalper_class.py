import requests
from bs4 import BeautifulSoup

HEADERS = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/84.0.4147.105 Safari/537.36', 'accept': '*/*'}  # Real params


class Scalper:

    def __init__(self, URL, item_1, item_2, item_3, item_4):
        self.URL = URL
        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3
        self.item_4 = item_4

    def parse(self, params=None):
        html = requests.get(self.URL, headers=HEADERS, params=params)
        print(html.status_code)
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', jscontroller_='LVJlx', class_=self.item_1)
        print(items.text)


milk = Scalper('https://play.google.com/store/apps/details?id=ru.more.play', 'UD7Dzf',0,0,0)
milk.parse()
