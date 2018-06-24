import requests
from bs4 import BeautifulSoup
import re

def get_rss_feed(website_url):
    if website_url is None:
        print("URL should not be null")
    else:
        source_code = requests.get(website_url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"lxml")
        for link in soup.find_all(attrs={'class': re.compile(r"follow-us__list-item-link$")}):
            href = link.get('href')
            print("RSS feed for " + website_url + "is -->  " + str(href))

get_rss_feed("https://www.bbc.com/news/uk/")
