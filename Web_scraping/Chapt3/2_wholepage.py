#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:07:26 2017

@author: changyueh
"""
#1. make sure there is no repeat scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages: #new pages
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('') #start with the main page

 #2. collect all data/info in website
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re 

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0]) #missing in some pages, need to add exception
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')
    
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('-------------------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')
    
                   

