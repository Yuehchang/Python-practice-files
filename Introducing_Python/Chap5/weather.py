#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 12:53:06 2017

@author: changyueh
"""

from sources import daily, weekly

print("Daily forecast:", daily.forecast())
print("Weekly forecast:", weekly.forecast())

for number, outlook in enumerate(weekly.forecast(),1):
    print (number, outlook)