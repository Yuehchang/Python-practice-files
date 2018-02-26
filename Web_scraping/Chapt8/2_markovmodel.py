#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:59:44 2018

@author: changyueh
"""

#Markov model 
from urllib.request import urlopen
from random import randint

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum 

def retrieveRandomWord(wordList):
    randIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randIndex -= value
        if randIndex <= 0:
            return word

def buildWordDict(text):
    #remove newlines and quotes
    text = text.replace('\n', ' ')
    text = text.replace('\"', '')
    
    #make sure the punctuation marks are treat as their own 'words'
    #so that they will be included in the Markov chain
    punctuation = [',', '.', ';', ':', '?']
    for symbol in punctuation:
        text = text.replace(symbol, ' '+symbol+' ')
    
    words = text.split(' ') #the works above are to prepare for this script
    words = [word for word in words if word != ''] #filter out empty words
    
    
    wordDict = dict()
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            #create a new dict for this word
            wordDict[words[i-1]] = dict()
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] += 1
    
    return wordDict 

text = str(urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(), 'utf-8')
wordDict = buildWordDict(text)

#create a Markov chain in length 100
length = 100
chain = ''
currentWord = 'I'
for i in range(0, length):
    chain += currentWord+' '
    currentWord = retrieveRandomWord(wordDict[currentWord])
print(chain)