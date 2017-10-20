#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 11:17:12 2017

@author: changyueh
"""

def get_description(): # see the docstring below
    """ Return random weather, just like the pros"""
    from random import choice 
    possibilities = ['snow', 'rain', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)