#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 17:54:28 2017

@author: changyueh
"""

#Media Files several pros and cons at page71-72
from urllib.request import urlretrieve #get files from any url
from urllib.request import urlopen
from bs4 import BeautifulSoup

#download single file 
html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html, 'lxml')
imageLocation = bsObj.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(imageLocation, 'logo.jpg')

#download multiple files 
import os 
from urllib.request import urlretrieve 
from urllib.request import urlopen
from bs4 import BeautifulSoup

downloadDirectory = 'downloaded'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteURL(baseUrl, source):
    if source.startwith('http://www.'):
        url = 'http://'+soruce[11:]
    elif source.startwith('http://'):
        url = source
    elif source.startwith('www.'):
        url = source[4:]
        url = 'http://'+url
    else:
        url = baseUrl+'/'+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replace('www.', '')
    path = path.replace(baseUrl, '')
    path = downloadDirectory+path
    directory = os.path.dirname(path)
    
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    return path

html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteURL(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
