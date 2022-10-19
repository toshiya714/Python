from operator import mod
import requests
import collections
from bs4 import BeautifulSoup
import os



class Scraper:
    collections.Callable = collections.abc.Callable
    
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        # collections.Callable = collections.abc.Callable
        res = requests.get(self.site)
        file_path = os.path.join("D:\Programming\Python", "text.txt")
        f = open(file_path, mode="w+")
        parser = "html.parser"
        sp = BeautifulSoup(res.text, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            f.write(str(url) + "\n")
            if url is None:
                continue
            if "https:" in url:
                print("\n" + url)
        f.close()

news = "https://news.google.com/"
Scraper(news).scrape()