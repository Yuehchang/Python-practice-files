#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 14:28:22 2018

@author: changyueh
"""

#Request package
import requests

##1. submit a form 
params = {'firstname': 'Ryan', 'lastname': 'Mitchell'}
r = requests.post('http://pythonscraping.com/files/processing.php', data=params)
print(r.text)

##2. second practice 
params = {'email_addr': 'cyueh1106@gmail.com'}
r = requests.post('http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi',
                  data=params)
print(r.text) 

##Radio Buttons, Checkbox and other input 

##Submitting files and images
files = {'uploadFile': open('/Users/changyueh/desktop/codepractice/web_scraping/chapt5/logo.jpg', 'rb')}
r = requests.post('http://pythonscraping.com/files/processing2.php', files=files)
print(r.text)

##Handling logins and cookies
params = {'username': 'yueh', 'password': 'password'}
r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=params)
print('Cookie is set to:')
print(r.cookies.get_dict())
print('------------')
print('Going to profile page...')
r = requests.post('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
print(r.text)

##a website which modifies cookies without warning?
session = requests.Session() #good function to fix this issue

params = {'username': 'yueh', 'password': 'password'}
#request => session
s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', data=params)

print('Cookie is set to:')
print(r.cookies.get_dict())
print('------------')
print('Going to profile page...')
#request => seesion
s = seesion.get('http://pythonscraping.com/pages/cookies/profile.php')

print(r.text)

##HTTP Basic access authentication page144
