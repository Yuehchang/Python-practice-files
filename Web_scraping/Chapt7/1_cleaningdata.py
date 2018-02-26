#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 14:36:50 2018

@author: changyueh
"""
#Cleaning in Code

##n-grams: practice 2-grams
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getNgrams(inputs, n):
    inputs = inputs.split(' ')
    output = []
    for i in range(len(inputs)-n+1):
        output.append(inputs[i:i+n])
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
ngrams = getNgrams(content, 2)
print(ngrams)
print('2-grams count is: '+str(len(ngrams)))
    
##clean the escape characters or Unicode characters
import re

def getNgrams(content, n):
    content = re.sub('\n+', ' ', content)
    content = re.sub(' +', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    print(content)
    content = content.split(' ')
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

##more rules to follow
##1. discard single character excluding 'i' or 'a'
##2. numbers enclosed in brackets should be discarded
##3. punctuation marks should also be discarded
import string

def cleanInput(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('[[0-9]*\]', '', input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.upper()
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

#Data normalization
from collections import OrderedDict 

def getDictNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        new_ngrams = ' '.join(input[i:i+n])
        if new_ngrams in output:
            output[new_ngrams] += 1
        else:
            output[new_ngrams] = 1
    return output

ngrams = getDictNgrams(content, 2)
ngrams1 = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
print(ngrams1)

#Cleaning after the fact page114
