#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:41:32 2018

@author: changyueh
"""

##Restare the kernel and verify the script
import pickle
import re
import os 
from vectorizer import vect 
import numpy as np

clf = pickle.load(open(os.path.join('pkl_objects', 'classifier.pkl'), 'rb'))

label = {0: 'negative', 1: 'positive'}

example = ['I love this movie']

X = vect.transform(example)

print('Prediction: {0}\nProbability: {1:.2f}%'.format(
        label[clf.predict(X)[0]],
        np.max(clf.predict_proba(X))*100))