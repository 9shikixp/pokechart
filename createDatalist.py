import sqlite3

con = sqlite3.connect('test.sqlite3')
cur = con.cursor()

cur.execute("select * from t_poke")
for row in cur:
	pokename = row[1]
	print("<option value=\"" + pokename + "\"></option>")