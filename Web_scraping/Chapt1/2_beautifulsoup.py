#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:04:00 2017

@author: changyueh
"""
#Build a reliable connection to scrap complete info or data
# Two commen errors will happen
# 1. Pages do not exist 
# 2. Can not find the server
# 3. No such Tag exist 
# Therefore, user need to consider what error might happen in case the web scraping stop to work.


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e: #(2)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1 #(3)
    except AttributeError as e:
        return None
    return title
title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)

