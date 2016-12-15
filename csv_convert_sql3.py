import sys
import csv
import sqlite3

con = sqlite3.connect('test.sqlite3')
cur = con.cursor()

cur.execute("""create table t_poke(
				id integer,
				name text,
				type text,
				hp integer,
				atk integer,
				def integer,
				satk integer,
				sdef integer,
				speed integer,
				total integer)""")

fp = open("test.csv")
pokelist = csv.reader(fp)

i = 0
for row in pokelist:
	i = i+1
	t = (i,
		row[0],
		row[1],
		row[2],
		row[3],
		row[4],
		row[5],
		row[6],
		row[7],
		row[8])
	cur.execute("insert into t_poke values(?,?,?,?,?,?,?,?,?,?)", t)

con.commit()
cur.close()