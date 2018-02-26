#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:37:01 2017

@author: changyueh
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'lxml')
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link.attrs['href']) #Tag: href will contain the links but some of them are useless

# 3 rules of the links we need in commen page33
for link in bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

# create a def to scrap links in the website and randomly select the connection links in it.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now()) #in order to make a different selection fo selecting links.
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org' + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href'] #https://docs.python.org/2/library/random.html
    print(newArticle)
    links = getLinks(newArticle)

