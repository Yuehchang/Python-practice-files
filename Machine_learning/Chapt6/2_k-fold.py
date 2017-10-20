#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:45:12 2017

@author: changyueh
"""
#data preprocessing
exec(open('1_pipelines.py').read())

#Usiing k-fold cross-validation to assess model performance

##the holdout method
"""
The purpose for using holdout method is when selecting the 
optimal value of tuning parameters(hyperparameters) it is not a 
good practice for using test-dataset over and over again.
"""

#stratified K-fold cross-validation
import numpy as np
from sklearn.cross_validation import StratifiedKFold
kfold = StratifiedKFold(y=y_train,
                        n_folds=10,
                        random_state=1)
scores = []
for k, (train, test) in enumerate(kfold):
    pipe_lr.fit(X_train[train], y_train[train])
    score = pipe_lr.score(X_train[test], y_train[test])
    scores.append(score)
    print('Fold: {0}, Class dist.: {1}, Acc: {2:.3f}'.format(k+1, 
          np.bincount(y_train[train]), score))
print('CV accuracy: {0:.3f} +/- {1:.3f}'.format(np.mean(scores), np.std(scores)))                        

#more efficiency way
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(estimator=pipe_lr,
                         X=X_train,
                         y=y_train,
                         cv=10,
                         n_jobs=1)
print('CV accuracy scores: {}'.format(scores))
print('CV accuracy: {0:.3f} +/- {1:.3f}'.format(np.mean(scores), np.std(scores)))
