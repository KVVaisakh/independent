import feedparser
import requests
from bs4 import BeautifulSoup
import os


def MakeXml2(rss):
	waste,name=rss.split("://")
	list=[]
	list=name.split("/")
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	f=open(os.path.join(BASE_DIR,"files/"+list[0]+".html"),'w')
	message=""
	info = feedparser.parse('http://www.reddit.com/.rss')
	for data in info.entries:
		message+=data.title
		soup = BeautifulSoup(data.description, 'html.parser')
		message+=(soup.prettify())
	f.write(message)
	print(message)
	f.close()
