#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:18:20 2017

@author: changyueh
"""
"""
Chapter 1 
"""
for countdown in 5,4,3,2,1, "hey!": 
    print(countdown)
    

#List []
cliches = [
        "At the end of the day",
        "Having said that",
        "The fact of the matter is",
        "Be that as it may",
        "The bottom line is",
        "If you will"
        ]
print(cliches[3])

#Dictionary {}
quotes = {
        "Moe" : "A wise guy, huh?",
        "Larry" : "Ow!",
        "Curly" : "Nyuk nyuk!"
        }
#key     #value
stooge = "Curly" 
print(stooge, "says:", quotes[stooge])

#Zen of Python!
import this