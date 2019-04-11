#!/usr/bin/python
# coding: utf8

from bs4 import BeautifulSoup
from urllib2 import urlopen
import urllib
import re
import os

def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c,'_')
    return value;

urlbase = 'multiki'
#urlbase = 'film'
#urlbase = 'filmiki'
basepath = os.path.join(os.getcwd(), 'ajlover_' + urlbase)
url = 'http://' + urlbase + '.arjlover.net'
httpstream = urlopen(url + '/' + urlbase)
#httpstream = open(os.path.join(os.getcwd(), 'mult.html')).read()
soup = BeautifulSoup(httpstream, "html.parser")
httpstream.close()

links = soup.find_all('td', 'l', text=re.compile(u'38'))

if len(links) == 0:
    showMessage('Error', 'Wrong page', 3000)
else:
    if not os.path.exists(basepath):
        os.makedirs(basepath)
    for link in links:
        try:
            titleText = remove(link.find('a').string.encode('utf-8'), '\/:*?"<>|')
            tds = link.findNextSiblings('td')
            href = (url + tds[-1].findAll('a')[-1]['href']).encode('utf-8')
            #print titleText + " - " + href
            strmfilename = os.path.join(basepath, titleText + '.strm')
            #print strmfilename
            f = open(strmfilename, 'w')
            f.write('plugin://plugin.video.elementum/play?uri=' + href)
            f.close()
            dirname = os.path.join(basepath, titleText)
            #os.makedirs(dirname)
            filename = os.path.join(dirname, os.path.split(href)[1])
            #print filename
            #urllib.urlretrieve(href, filename)
        except:
            pass
