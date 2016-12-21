# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:27:24 2016

@author: Danik
"""
import cgi
import sqlite3

conn = sqlite3.connect('db_org')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Organizations')
cur.execute('DROP TABLE IF EXISTS Middle')

sql1 = '''CREATE TABLE Organizations (
id INTEGER PRIMARY KEY AUTOINCREMENT, 
name TEXT,
district TEXT,
site TEXT,
email TEXT,
time TEXT)'''
cur.execute(sql1)

sql2 = '''CREATE TABLE Middle (
name TEXT,
phone TEXT)'''
cur.execute(sql2)
conn.commit()

html = """Content-type: text/html

<HTML>
<BODY>
<H1>Result</H1>
<P>
%s
</BODY>
</HTML>
"""
print(html % 'Data Base sucsessfuly created!')