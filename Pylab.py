import urllib.request
import self as self
from bs4 import BeautifulSoup

class Data_Repository(object):
    def __init__(self, listik):
        pass
    self.listik = []
    def parse_site(self)
        o = urllib.request.urlopen('https://www.citilink.ru/catalog/audio_and_digits/tv/1079079/')
        html = BeautifulSoup(o.read(), "lxml")

        spans = html.find_all('div', {'class': 'price price_break'})

        for span in spans:
            print(span)
    def save_to_file()
        f = open('list.txt')
        f
        f.close()
