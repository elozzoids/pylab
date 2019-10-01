import urllib.request
from bs4 import BeautifulSoup
o = urllib.request.urlopen('https://www.citilink.ru/catalog/audio_and_digits/tv/1079079/')

html_text = """<span class="_2a97c9"> 990&nbsp;₽ </span>"""


html = BeautifulSoup(o.read(), "lxml")

spans = html.find_all('div', {'class': 'price price_break'})

for span in spans:
    print(span)
