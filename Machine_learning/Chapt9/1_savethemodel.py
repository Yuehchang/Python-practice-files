#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 15:31:08 2018

@author: changyueh
"""

#Serializing fitted scikit-learn estimators
##1. reload the out-of-score model 
exec(open('/users/changyueh/desktop/codepractice/machine_learning/chapt8/3_outofcorelearning.py').read())

import pickle
import os 
dest = os.path.join('/users/changyueh/desktop/codepractice/machine/movieclassifier', 'pkl_objects')
if not os.path.exists(dest):
    os.makedirs(dest)
pickle.dump(stop, open(os.path.join(dest, 'stopwords.pkl'), 'wb'), protocol=4)
pickle.dump(clf, open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol=4)

##create a new vectorizer page253