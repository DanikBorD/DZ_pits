# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:20:17 2016

@author: Danik
"""
import cgi
html = """Content-type: text/html

<HTML>
<BODY>
<H1>Sum</H1>
<P>
%s
</BODY>
</HTML>
"""
form = cgi.FieldStorage()

if not ('first' or 'second') in form:
    print(html % 'where are your numbers, bitch?!')
else:
    first = int(form['first'].value)
    second = int(form['second'].value)
    summ = first+second
    text = str(summ)
    print(html %text)
