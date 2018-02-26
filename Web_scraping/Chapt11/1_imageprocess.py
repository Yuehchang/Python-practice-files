#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:15:53 2018

@author: changyueh
"""
#Pillow
from PIL import ImageFilter
from PIL import Image #unable to import Image, still need to figure out this issue

path = r'/Users/changyueh/Desktop/CodePractice/Web_scraping/Chapt5/logo.jpg'
Logo = Image.open(path)
blurryLogo = Logo.filter(ImageFilter.GaussianBlur)
blurryLogo.save('logo_blurred.jpg')
blurryLogo.show()


