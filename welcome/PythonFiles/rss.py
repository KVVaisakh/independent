"""import feedparser"""
import requests
from bs4 import BeautifulSoup
import os


def MakeXml(rss):
	source_code = requests.get(rss)
	message = source_code.text
	waste,name=rss.split("://")
	list=[]
	list=name.split("/")
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	f=open(os.path.join(BASE_DIR,"files/"+list[0]+".html"),'w')
	f.write(message)
	print("Success!!!")
	f.close()
	return list[0]
