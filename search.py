#!/usr/bin/python3
import requests,bs4,webbrowser,sys,time,re
from urlextract import URLExtract
sterm=' '.join(sys.argv[1:])
res=requests.get('https://www.google.co.jp/search?q='+sterm)
res.raise_for_status()
bso=bs4.BeautifulSoup(res.text,"lxml")
linkeles=bso.select('.r a')
extractor = URLExtract()
urls = extractor.find_urls(linkeles[1].get("href"))
print(urls[0].split("&")[0])
time.sleep(0.5)

