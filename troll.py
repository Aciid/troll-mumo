import feedparser, random, urllib,base64
from BeautifulSoup import BeautifulSoup

d = feedparser.parse('http://imgur.com/r/all/rss')
rand = random.randint(1,10)
crap = d.entries[rand].description

soup = BeautifulSoup(crap)
link = soup.findAll('img')[0]['src']
img = urllib.urlopen(link)
encoded = base64.b64encode(img.read())

s1.sendMessageChannel(2,1,'<img src="data:image/jpeg;charset=utf-8;base64,' + str(encoded) + '"/><a href=' + link +'>'+link+'</a>')
