import sqlite3

con = sqlite3.connect('test.sqlite3')
cur = con.cursor()

cur.execute("select * from t_poke")
