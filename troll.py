import feedparser, random, urllib, base64
from BeautifulSoup import BeautifulSoup
from random import choice

def getPile():
        global l, d
        l = ['wtf','nsfw','spacedicks','clopclop'] # need more pull-requests.
        d = feedparser.parse('http://imgur.com/r/'+choice(l)+'/rss')
        return l
        return d

def digDeeper(debug):
        global link
        rand = random.randint(1,10)
        crap = d.entries[rand].description
        soup = BeautifulSoup(crap)
        link = soup.findAll('img')[0]['src']
        if debug == 1:
                print link

def satisfyMistress():
        while link.find('.gif') == '-1': # lel QT-gifu render shit.
                digDeeper()

def munchies():
        img = urllib.urlopen(link)
        encoded = base64.b64encode(img.read())

def soloMidOrFeed():
        s1.sendMessageChannel(2,1,'<img src="data:image/jpeg;charset=utf-8;base64,' + str(encoded) + $

if __name__ == '__main__':
        getPile()
        digDeeper(1)
        satisfyMistress()
        munchies()
        soloMidOrFeed()


