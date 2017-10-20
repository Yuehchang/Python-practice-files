#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 12:10:04 2017

@author: changyueh
"""

import sqlite3
query="""
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
c REAL,         d INTEGER
); """ #建立table
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit() #以上使用sqlite3驅動器

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'F;orida', 2.6, 3),
        ('Scramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()

