#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:02:06 2018

@author: changyueh
"""

#Text
from urllib.request import urlopen
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1.txt')
print(textPage.read())

##Encoding practice 
textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(textPage.read())

textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')
print(str(textPage.read(), 'utf-8')) #check meta for the encoding

#CSV
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
    print(row)

for row in csvReader:
    print('The album \"'+row[0]+'\" was released in '+str(row[1]))
    
##DictReader: dealing with the header
data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)   
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)

for row in dictReader:
    print('The album \"'+row['Name']+'\" was released in '+row['Year'])
    
#PDF
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
from urllib.request import urlopen

def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    
    process_pdf(rsrcmgr, device, pdfFile)
    
    content = retstr.getvalue()
    retstr.close()
    return content

pdfFile = urlopen('http://pythonscraping.com/pages/warandpeace/chapter1.pdf')
outputString = readPDF(pdfFile)
print(outputString)
pdfFile.close()

##practice
pdfFile_local = open('/Users/changyueh/Desktop/UConn/17 insurence.pdf', 'rb')
outputString = readPDF(pdfFile_local)
print(outputString)
pdfFile.close()

#MS word 
from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO

wordFile = urlopen('http://pythonscraping.com/pages/AWordDocument.docx').read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

print(xml_content.decode('utf-8'))

##<w:t> => the context 
from bs4 import BeautifulSoup

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'lxml')
text_Strings = wordObj.findAll('w:t')

for textElem in text_Strings:
    print(textElem.text) #could add some exception for the scraper page106
    