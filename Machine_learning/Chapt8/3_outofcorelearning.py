#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 17:33:41 2018

@author: changyueh
"""
import numpy as np
import re
import pyprind
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier

stop = stopwords.words('english')

#build clean text 
def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

#def for read one document at a time
def stream_docs(path):
    with open(path, 'r', encoding='utf-8') as csv:
        next(csv) #skip header
        for line in csv:
            text, label = line[:-3], int(line[-2])
            yield text, label

##verify the function
next(stream_docs(path='/users/changyueh/desktop/codepractice/machine_learning/chapt8/movie_data.csv'))

#def for returning particular number of docs by the size parameter
def get_minibatch(doc_stream, size):
    docs, y = [], []
    try:
        for _ in range(size):
            text, label = next(doc_stream)
            docs.append(text)
            y.append(label)
    except StopIteration:
        return None, None
    return docs, y

#HashingVectorizer => not able to use the previous vectorizers (reason in page p247)
vect = HashingVectorizer(decode_error='ignore',
                         n_features=2**21,
                         preprocessor=None,
                         tokenizer=tokenizer)
clf = SGDClassifier(loss='log', random_state=1, n_iter=1)
doc_stream = stream_docs(path='/users/changyueh/desktop/codepractice/machine_learning/chapt8/movie_data.csv')
#Start the out-of-core learning
pbar = pyprind.ProgBar(45)
classes = np.array([0, 1])
for _ in range(45):
    X_train, y_train = get_minibatch(doc_stream, size=1000)
    if not X_train:
        break
    X_train = vect.transform(X_train)
    clf.partial_fit(X_train, y_train, classes=classes)
    pbar.update()

##fit the test
X_test, y_test = get_minibatch(doc_stream, size=5000)
X_test = vect.transform(X_test)    
print('Accuracy: {:.3f}'.format(clf.score(X_test, y_test)))
