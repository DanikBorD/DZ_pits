# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 20:14:09 2016

@author: Danik
"""

import sqlite3

conn = sqlite3.connect('db_org')
cur = conn.cursor()

d=[]

cur.execute('SELECT name FROM Organizations')
for row in cur.fetchall():
    d.append(row[0])
    
html = """Content-type: text/html

<HTML>
<BODY>
<H1>List of organizations</H1>
<P>
%s
</BODY>
</HTML>
"""
text = ''
for i in range(len(d)):
    text += str(d[i]) 
    text += '<P>'
    
print (html % text)