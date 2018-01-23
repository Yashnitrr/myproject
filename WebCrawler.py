import requests
from bs4 import BeautifulSoup

def trade_spider(url):
   # page = 1
   # while page <= max_page:
   # url = "http://www.tvguide.com/listings/"
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('span',{'class':'listings-program'}):
          #  href = link.get('href')
            print(link)
       # page+=1

trade_spider("http://www.tvguide.com/listings/")
