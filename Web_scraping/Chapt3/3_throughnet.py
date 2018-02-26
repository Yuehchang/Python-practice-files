#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 22:11:41 2017

@author: changyueh
"""

from urllib.request import urlopen, urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#collect the internal links in the site
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    
    #find all the links started with "/"
    for link in bsObj.findAll('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

#collect the external links in the site
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    
    #find all the links started with 'http' or 'wwww' but not include the present URL
    for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace('http://', '').split('/')
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, 'lxml')
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc) #urlparse doc. => https://docs.python.org/2/library/urlparse.html 
    
    #Find no external links and pick one in the site
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = urlparse(startingPage).scheme+'://'+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external links is:' + externalLink)
    followExternalOnly(externalLink)
    
followExternalOnly('http://oreilly.com')

#goal = scraping all external links and record those links
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj, splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            print('About to get link: '+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)
getAllExternalLinks('http://oreilly.com')