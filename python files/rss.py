import feedparser
from bs4 import BeautifulSoup

f=open('soup.html','w')
message=""
info = feedparser.parse('http://www.reddit.com/.rss')
for data in info.entries:
	message+=data.title
	soup = BeautifulSoup(data.description, 'html.parser')
	message+=(soup.prettify())
f.write(message)
f.close()
