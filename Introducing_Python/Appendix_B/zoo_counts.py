#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 14:41:42 2017

@author: changyueh
"""

import csv
from collections import Counter

counts = Counter()

with open('zoo.csv', 'rt') as fin:
    cin = csv.reader(fin)
    for num, row in enumerate(cin):
        if num > 0:
            counts[row[0]] += int(row[-1]) #counts[row(0)] = counts[row(0)] + int(row[-1])
for animal, hush in counts.items():
    print("%10s %10s" % (animal, hush)) #Counter出的結果是Dictionary