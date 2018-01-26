#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:52:52 2017

@author: changyueh
"""
#Opinion mining in IMDb reviews

import pyprind 
import pandas as pd
import os 
import numpy as np

pbar = pyprind.ProgBar(50000)
labels = {'pos':1, 'neg':0}
df = pd.DataFrame()
for s in ('test', 'train'):
    for l in ('pos', 'neg'):
        path ='/users/changyueh/desktop/codepractice/machine_learning/chapt8/aclImdb/{0}/{1}'.format(s, l)
        for file in os.listdir(path):
            with open(os.path.join(path, file), 'r') as infile:
                txt = infile.read()
            df = df.append([[txt, labels[l]]], ignore_index=True)
            pbar.update() #update the process 
df.columns = ['review', 'sentiment']

#shuffle the DataFrame
np.random.seed(0)
df = df.reindex(np.random.permutation(df.index))
df.to_csv('/users/changyueh/desktop/codepractice/machine_learning/chapt8/movie_data.csv', index=False)
