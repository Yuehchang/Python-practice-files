#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 17:26:33 2017

@author: changyueh
"""

#Echo Nest practice -> https://developer.echonest.com/account/register

#Twitter practice => lib:github.com/sixohsix/twitter/tree/master
from twitter import Twitter, OAuth
t = Twitter(auth=OAuth('946515129151172608-rrKhj2bHXfTiPYD0qX3o71RDhXF0J7z', 'avPH0cCE4tYvBjsS695QpeUMrOvwyrPGXQ7uXg7LDv67D',
                       'rMdcSjNk8rxQcEp4FEQDWcOoM', 'wpZsgySHqjdb5xhimLl9UJqkakfD0SZU8uDvHxxkyQzGzwAxGa'))
pythonTweets = t.search.tweets(q='#python')
print(pythonTweets)

#using python and twitter application to tweet!
t = Twitter(auth=OAuth('946515129151172608-rrKhj2bHXfTiPYD0qX3o71RDhXF0J7z', 'avPH0cCE4tYvBjsS695QpeUMrOvwyrPGXQ7uXg7LDv67D',
                       'rMdcSjNk8rxQcEp4FEQDWcOoM', 'wpZsgySHqjdb5xhimLl9UJqkakfD0SZU8uDvHxxkyQzGzwAxGa'))
statusUpdate = t.statuses.update(status='Hello, world!')
print(statusUpdate)

#limit the response numbers
pythonStatuses = t.statuses.user_timeline(screen_name='montpython', count=5)
print(pythonStatuses)

#Google API

#json 
import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get('country_code')
print(getCountry('50.78.253.58'))

##json practice 
jsonString = '''{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],
                 "arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'''
jsonObj = json.loads(jsonString)

print(jsonObj.get('arrayOfNums'))
print(jsonObj.get('arrayOfNums')[1])
print(jsonObj.get('arrayOfNums')[1].get('number'))
print(jsonObj.get('arrayOfFruits')[2].get('fruit'))

#combine API with web scraping
from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
import json
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    #the format for links of edition pages
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title='+pageUrl+'&action=history'
    print('history url is: '+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    #find the links in class 'mw-anonuserlink': need to find IPs not login name
    ipAddresses = bsObj.findAll('a', {'class': 'mw-userlink mw-anonuserlink'})
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

links = getLinks('/wiki/Python_(programming_language)')

while(len(links)>0):
    for link in links:
        print('-------------------------------')
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            print(historyIP)
    newLink = links[random.randint(0, len(links)-1)].attr['href']
    links = getLinks(newLink)

#get the ipaddress 
def getCountry(ipAddress):
    try:
        response = urlopen('http://freegeoip.net/json/'+ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')

links = getLinks('/wiki/Python_(programming_language)')

while(len(links)>0):
    for link in links:
        print('-------------------------------')
        historyIPs = getHistoryIPs(link.attrs['href'])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print(historyIP+' is from '+country)
    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)            