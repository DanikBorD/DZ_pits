# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:31:28 2016

@author: Danik
"""
import cgi
import sqlite3
import hashlib

msg = hashlib.md5()
conn = sqlite3.connect('db_html')
cur = conn.cursor()
#keys = '''PRAGMA FOREIGN_KEYS=ON'''
#cur.execute(keys)
html = """Content-type: text/html

<HTML>
<BODY>
<H1>Добавление в таблицу Users</H1>
<P>
%s
</BODY>
</HTML>
"""
form = cgi.FieldStorage()

if not ('name' or 'email' or 'pass') in form:
    print(html % 'where are your data, bitch?!')
else:
    msg.update(str(form['pass'].value)).encode()
    hash_pass = msg.hexdigest()
    cur.execute('INSERT INTO Users(name, email, pass) VALUES(?,?,?)', (form['name'].value,form['email'].value,hash_pass))
    conn.commit()
    text = 'User successfuly added!'
    print(html % text)

