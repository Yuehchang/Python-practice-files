#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:42:03 2017

@author: changyueh
"""

#Storing data to CSV
#Download directly without any modification
import csv

csvFile = open('/Users/changyueh/Desktop/CodePractice/Web_scraping/Chapt5/test.csv', 'w+', newline='')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
finally:
    csvFile.close()
    
#practice 
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bsObj = BeautifulSoup(html, 'lxml')
#first table in this link
table = bsObj.findAll('table', {'class': 'wikitable'})[0]
rows = table.findAll('tr')

csvFile = open('/Users/changyueh/Desktop/CodePractice/Web_scraping/Chapt5/editors.csv', 'wt', newline='', encoding='utf-8')
try:
    writer = csv.writer(csvFile)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()