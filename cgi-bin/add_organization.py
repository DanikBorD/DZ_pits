# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:57:10 2016

@author: Danik
"""

import cgi
import sqlite3

conn = sqlite3.connect('db_org')
cur = conn.cursor()
#keys = '''PRAGMA FOREIGN_KEYS=ON'''
#cur.execute(keys)
html = """Content-type: text/html

<HTML>
<BODY>
<H1>Добавление в таблицу Organizations</H1>
<P>
%s
</BODY>
</HTML>
"""
form = cgi.FieldStorage()

#cur.execute('SELECT name FROM Organizations')

#print(max_id)
d=[]
if not ('name' or 'district' or 'phone' or 'site' or 'email' or 'time') in form:
    print(html % 'where are your data, bitch?!')
else:
    phone = str(form['phone'].value)
    phone_cor = phone.split(',')
    for k in range(len(phone_cor)):
         cur.execute('INSERT INTO Middle(name, phone) VALUES(?,?)', (form['name'].value, phone_cor[k]))
    cur.execute('INSERT INTO Organizations(name, district, site, email, time) VALUES(?,?,?,?,?)', (form['name'].value,form['district'].value,form['site'].value,form['email'].value,form['time'].value))
    conn.commit()
    text = 'Organization successfuly added!'
    print(html % text)