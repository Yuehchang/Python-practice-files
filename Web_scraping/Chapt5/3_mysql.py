#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:59:47 2018

@author: changyueh
"""
#sudo /usr/local/mysql/support-files/mysql.server start

import pymysql
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock',
                       user='root', password='813', db='mysql')
cur = conn.cursor()
cur.execute('USE scraping') 
cur.execute('SELECT * FROM pages WHERE id = 1')
print(cur.fetchone())
cur.close()
conn.close()

#store the data into db
#1. alter unicode to set the preparation
#2. scraping script
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', 
                       user='root', password='813', db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

random.seed(datetime.datetime.now())

def store(title, content):
    cur.execute('INSERT INTO pages (title, content)' + 'VALUES("{0}", "{1}")'.format(title, content))
    cur.connection.commit() #need add commit() to comfirm the update /rollback to discard 

def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org'+articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div', {'id': 'mw-content-text'}).find('p').get_text()
    store(title, content)
    return bsObj.find('div', {'id': 'mw-content-text'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon') #Six Degrees of Kevin Bacon

try:
    while(len(links)>0):
        newArticle = links[random.randint(0, len(links)-1)].attr['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()

#good reading material: http://bit.ly/1KHzoga
    
#MySQL six degree relationship links 
#1. create wikipedia db and two table in mysql
#2. scraping links which Bacon number is lower or equal than six
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', 
                          passwd='813', db='mysql', charset='utf8')

cur = conn.cursor()
cur.execute('USE wikipedia')

def pageScraped(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    if cur.rowcount == 0:
        return False
    page = cur.fetchone()
    
    cur.execute('SELECT * FROM links WHERE fromPageId = %s', (int(page[0])))
    if cur.rowcount == 0:
        return False
    return True

def insertPageIfNotExists(url):
    cur.execute('SELECT * FROM pages WHERE url = %s', (url))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO pages (url) VALUES (%s)', (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0] #return the last row which is already exist

def insertLink(fromPageId, toPageId):
    cur.execute('SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s', (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute('INSERT INTO links (fromPageId, toPageId) VALUES (%s, %s)', (int(fromPageId), int(toPageId)))
        conn.commit()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    for link in bsObj.findAll('a', href=re.compile('^(/wiki/)((?!:).)*$')):
        insertLink(pageId, insertPageIfNotExists(link.attrs['href']))
        if not pageScraped(link.attrs['href']):
            # => if not True(which means it is a new link for db)
            newPage = link.attrs['href']
            print(newPage)
            getLinks(newPage, recursionLevel+1)
        else:
            print('Skipping: '+str(link.attrs['href'])+' found on '+pageUrl) #statement of a link which already exists

getLinks('/wiki/Kevin_Bacon', 0)
cur.close()
conn.close()

"""
InternalError: (1267, "Illegal mix of collations (latin1_swedish_ci,IMPLICIT) and (utf8_general_ci,COERCIBLE) for operation '='")

=> error need fixed 
"""