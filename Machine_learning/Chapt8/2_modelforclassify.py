#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:49:56 2018

@author: changyueh
"""

#Training Logistic regression model for document classification
import re
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('/users/changyueh/desktop/codepractice/machine_learning/chapt8/movie_data.csv')

##practice 1. Bag-of-words model // n-grams' frequency 
count = CountVectorizer()
docs = np.array([
        'The sun is shining',
        'The weather is sweet',
        'The sun is shining and the weather is sweet'])
bag = count.fit_transform(docs)
print(count.vocabulary_)
print(bag.toarray())

##practice 2. term frequency-inverse document frequency
tfidf = TfidfTransformer()
np.set_printoptions(precision=2) #These options determine the way floating point numbers, arrays and other NumPy objects are displayed
print(tfidf.fit_transform(count.fit_transform(docs)).toarray())

#Cleaning text data
df.loc[0, 'review'][-50:]

def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ''.join(emoticons).replace('-', '')
    return text

##confirm the preprocessor works
preprocessor(df.loc[0, 'review'][-50:])
preprocessor('</a>This :) is :( a test :-)!')

##apply to our df
df['review'] = df.review.apply(preprocessor)

#Processing documents into tokens
def tokenizer(text):
    return text.split()

tokenizer(df.iloc[1, 0])

##Porter stemmer // Snowball stemmer or Lancaster stemmer (http://www.nltk.org/api/nltk.stem.html)
porter = PorterStemmer()
def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split()]
tokenizer_porter(df.iloc[1, 0])

##stop-word removal (in NLTK library)
nltk.download('stopwords') #download the dataset

stop = stopwords.words('english')
[w for w in tokenizer_porter(df.iloc[1, 0]) if w in stop]


#train and test ds
X_train = df.loc[:25000, 'review'].values
y_train = df.loc[:25000, 'sentiment'].values
X_test = df.loc[25000:, 'review'].values
y_test = df.loc[25000:, 'sentiment'].values

#GridSearch for best parameter and 5-folds
tfidf = TfidfVectorizer(strip_accents=None, lowercase=False, preprocessor=None)
param_grid = [{'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]},
              {'vect__ngram_range': [(1, 1)],
               'vect__stop_words': [stop, None],
               'vect__tokenizer': [tokenizer, tokenizer_porter],
               'vect__use_idf': [False],
               'vect__norm': [None],
               'clf__penalty': ['l1', 'l2'],
               'clf__C': [1.0, 10.0, 100.0]}]
lr_tfidf = Pipeline([('vect', tfidf),
                     ('clf', LogisticRegression(random_state=0))])
gs_lr_tfidf = GridSearchCV(lr_tfidf, param_grid,
                           scoring='accuracy',
                           cv=5, verbose=20,
                           n_jobs=-1)

gs_lr_tfidf.fit(X_train, y_train) #more than 40 mins => 2 hours and 20 mins

print('Best parameter set: {}'.format(gs_lr_tfidf.best_params_))
print('CV Accuracy: {:.3f}'.format(gs_lr_tfidf.best_score_))
clf = gs_lr_tfidf.best_estimator_
print('Test Accuracy: {:.3f}'.format(clf.score(X_test, y_test)))