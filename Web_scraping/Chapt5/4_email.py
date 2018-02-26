#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 12:45:24 2018

@author: changyueh
"""

import smtplib
from email.mime.text import MIMEText

msg = MIMEText('The body of the email is here')

msg['Subject'] = 'An Email Alert'
msg['From'] = 'cyueh1106@gmail.com'
msg['To'] = 'yueh.chang@uconn.edu'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

"""
ConnectionRefusedError: Connection refused
=> need to fix this issue
"""