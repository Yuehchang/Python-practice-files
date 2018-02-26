#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 13:32:54 2018

@author: changyueh
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    input = re.sub('\n+', ' ', input).lower()
    input = re.sub('[[0-9]*\]', ' ', input) #unnessary in this context
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'UTF-8')
    input = input.decode('ascii', 'ignore')
    cleanInput = []
    input = input.split(' ')
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput 

def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        ngramTemp = ' '.join(input[i:i+n])
        if ngramTemp not in output: 
            output[ngramTemp] = 0
        output[ngramTemp] += 1 #do not need to write down else statement 
    return output 

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = getNgrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)
print(sortedNGrams)

##get rid of the unwanted words 
def isCommen(ngarm):
    commenWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say", 
                   "this", "they", "is", "an", "at", "but","we", "his", "from", 
                   "that", "not", "by", "she", "or", "as", "what", "go", "their",
                   "can", "who", "get", "if", "would", "her", "all", "my", "make", 
                   "about", "know", "will", "as", "up", "one", "time", "has", "been", 
                   "there", "year", "so", "think", "when", "which", "them", "some", 
                   "me", "people", "take", "out", "into", "just", "see", "him", 
                   "your", "come", "could", "now", "than", "like", "other", "how",
                   "then", "its", "our", "two", "more", "these", "want", "way", "look", 
                   "first", "also", "new", "because", "day", "more", "use", "no", "man", 
                   "find", "here", "thing", "give", "many", "well"]
    for word in ngarm:
        if word in commenWords:
            return True
    return False
        
def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):        
        words = input[i:i+n] ###
        if isCommen(words): continue ###apply the isCommen function   
        ngramTemp = ' '.join(words)
        if ngramTemp not in output: 
            output[ngramTemp] = 0
        output[ngramTemp] += 1 #do not need to write down else statement 
    return output 

content = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
ngrams = getNgrams(content, 2)
sortedNGrams = sorted(ngrams.items(), key = operator.itemgetter(1), reverse=True)

for ngram, count in sortedNGrams:
    if count > 2:
        print("('{0}', {1})".format(ngram, count))
    