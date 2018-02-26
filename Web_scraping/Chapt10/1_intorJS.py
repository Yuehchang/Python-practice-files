#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 17:28:37 2018

@author: changyueh
"""

#JavaScript
#Package of JS

##jQuery page149 => the most popular function package among websites

##Google Analytics page150 => tracking tool

##Google Maps
###reverse Geocoding => reverse the pin code to address 

##Ajax / Dynamic HTML page151

##Selenium
###PhantomJS

from selenium import webdriver
import time 

driver = webdriver.PhantomJS(executable_path='/Users/changyueh/anaconda/bin/phantomjs')
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')