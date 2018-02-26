#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 17:05:12 2018

@author: changyueh
"""

#Natural Language Toolkit
from nltk import word_tokenize
from nltk import Text
from nltk.book import * #import text example from nltk database
from nltk import FreqDist 
from nltk import bigrams #same as 2-grams
from nltk import ngrams
from nltk import pos_tag

##
tokens = word_tokenize('Here is some not very interesting text')
text = Text(tokens)

words = []
for word in text6:
    if word not in words:
        words.append(word)

len(text6) / len(words)
    
#check the frequency
fdist = FreqDist(text6)        
fdist.most_common(10)
fdist['Grail']

#2-grams
bigrams = bigrams(text6)
bigramsDist = FreqDist(bigrams)
bigramsDist[('Sir', 'Robin')]

#n-grams
fourgrams = ngrams(text6, 4)
fourgramsDist = FreqDist(fourgrams)
fourgramsDist[('father', 'smelt', 'of', 'elderberries')]

for fourgram in fourgrams:
    if fourgram[0] == 'coconut':
        print(fourgram)

##Dicitionary in NLTK
text = word_tokenize('''Strange women lying in ponds distributing swords is no basis for a system of
                     government. Supreme executive power derives from a mandate from the masses, not 
                     from some farciacal aquatic ceremony.''')
pos_tag(text)

text2 = word_tokenize('''He was objective in achieving his objective of writing and objective philosophy,
                      primarily using verbs in the objective case.''')
pos_tag(text2)

##Why NLTK is useful in web scraping?
from nltk import word_tokenize, sent_tokenize, pos_tag
sentences = sent_tokenize('''Google is one of the best companies in the world.
                         I constantly google myself to see what I'm up to.''')
nouns = ['NN', 'NNS', 'NNP', 'NNPS']

for sentence in sentences:
    if 'google' in sentence.lower():
        taggedWords = pos_tag(word_tokenize(sentence))
        for word in taggedWords:
            if word[0].lower() == 'google' and word[1] in nouns:
                print(sentence)