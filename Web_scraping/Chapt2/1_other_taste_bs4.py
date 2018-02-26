#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 20:36:44 2017

@author: changyueh
"""
#1. Practice.A
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'lxml')

nameList = bsObj.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text()) #Should use .get_text at the last step of scraping. Must keep the Tag as long as possible.

#2. find() and findAll() page16

nameList = bsObj.findAll(text='the prince')
print(len(nameList)) #text will return the value you input

allText = bsObj.findAll(id='text')
print(allText[0].get_text()) #keyword: select specific tag

#3. Navigating Tree
##a. children and descendants
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'lxml')

for child in bsObj.find('table', {'id': 'giftList'}).children:
    print(child)
    
for descendant in bsObj.find('table', {'id': 'giftList'}).descendants:
    print(descendant) #different btw children and descendants

##b. siblings
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'lxml')

for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling) #good way to extract data without title 
    #previous_siblings / previous_sibling / next_siblings / next_sibling

#c. parent
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'lxml')

print(bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()) #explanation at page22

#4. Regex
##a. practice to write the regex email [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|edu|org|net)
##b. Regex and bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'lxml')
images = bsObj.findAll('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})
for image in images:
    print(image)

#5. Lambda page28
