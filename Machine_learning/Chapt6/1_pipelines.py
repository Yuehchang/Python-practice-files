#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:22:55 2017

@author: changyueh
""" 
#Loading the Breast Cancer Wisconsin dataset
"""
Data description:
ID, diagnosis=(M:malignant, B=benign)
剩下的columns => real-value features for digitized images of cell識別是M/B
"""
##1. read the dataset
import pandas as pd
path = 'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data'
df = pd.read_csv(path, header=None)

##2. assign 30 features to NumPy array X / and use LabelEncoder
from sklearn.preprocessing import LabelEncoder
X = df.loc[:, 2:].values #所以返回不是df，要加上values
y = df.loc[:, 1].values #返回object
le = LabelEncoder()
y = le.fit_transform(y) #返回NumPy array
le.transform(['M', 'B']) #可以查看M/B被指派成什麼

##3. divide into training(80%) and testing(20%)
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.20, random_state=1) #random_state指派數值是為了讓每次返回的都一樣，如果是None每次的split都不同

#Combining transformers and estimators in a pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
pipe_lr = Pipeline([('scl', StandardScaler()),
                    ('pca', PCA(n_components=2)),
                    ('clf', LogisticRegression(random_state=1))])
pipe_lr.fit(X_train, y_train)
print('Test Accuracy: {}'.format(pipe_lr.score(X_test, y_test)))

#page172 the concept of how pipelines work is.