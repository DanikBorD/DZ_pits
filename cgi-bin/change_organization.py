import cgi
import sqlite3

conn = sqlite3.connect('db_org')
cur = conn.cursor()

d=[]
l=[]

form = cgi.FieldStorage()

cur.execute('SELECT name, district, site, email, time FROM Organizations WHERE name=?',[form['name'].value])
for row in cur.fetchall():
    for k in range(len(row)):
        d.append(row[k])

cur.execute('SELECT * FROM Middle WHERE name=?',[form['name'].value])
row2 = cur.fetchall()

for k in range(len(row2)):
    l.append(row2[k][1])
phones = ''
for k in range(len(l)):
    phones += str(l[k]) + ','
print ("""
<HTML>
<BODY>
<form method=GET action="add_organization.py">
<P>
<B>Enter organization name: </B>
<P>
<input type=text name=name value=""" + d[0] + """>
<P>
<B>Enter index: </B>
<P>
<input type=text name=district value=""" + d[1] + """>
<P>
<B>Enter phone: </B>
<P>
<input type=text name=phone value=""" + phones + """>
<P>
<B>Enter site: </B>
<P>
<input type=text name=site value=""" + d[2] + """>
<P>
<B>Enter email: </B>
<P>
<input type=text name=email value=""" + d[3] + """>
<P>
<B>Enter time: </B>
<P>
<input type=text name=time value=""" + d[4] + """>
<P>
<input type=submit value="Change">
</form>
</BODY>
</HTML>
""")
cur.execute('DELETE FROM Organizations WHERE name=?', [form['name'].value])
cur.execute('DELETE FROM Middle WHERE name=?', [form['name'].value])
conn.commit()

