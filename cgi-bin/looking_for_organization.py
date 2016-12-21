# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:02:12 2016

@author: Danik
"""

import cgi
import sqlite3

conn = sqlite3.connect('db_org')
cur = conn.cursor()

html = """
<HTML>
<BODY>
<P>
%s
</BODY>
</HTML>
"""
form = cgi.FieldStorage()
named = ['name', 'district', 'site', 'email', 'time']
d = []

cur.execute('SELECT name, district, site, email, time FROM Organizations WHERE name=?',[form['name'].value])
for row in cur.fetchall():
    for k in range(len(row)):
        d.append(row[k])
text = ''
for i in range(len(d)-1):
    text += str(named[i]) + ': ' + str(d[i])
    text += '<P>'

print(html % text)


cur.execute('SELECT * FROM Middle WHERE name=?',[form['name'].value])
row2 = cur.fetchall()

print(html % 'phones: ')
for k in range(len(row2)):
    print(html % row2[k][1])

    