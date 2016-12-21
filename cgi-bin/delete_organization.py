import cgi
import sqlite3

conn = sqlite3.connect('db_org')
cur = conn.cursor()

form = cgi.FieldStorage()

cur.execute('DELETE FROM Organizations WHERE name=?', [form['name'].value])
cur.execute('DELETE FROM Middle WHERE name=?', [form['name'].value])
conn.commit()

html = """
<HTML>
<BODY>
<P>
%s
</BODY>
</HTML>
"""
print(html % 'Organization sucsessfuly deleted!')