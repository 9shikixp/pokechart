from flask import Flask
from flask import render_template
from flask import request
import sqlite3
import numpy as np
import typechart
app = Flask(__name__)

def addstr(row):
	pokedata = ""
	for d in row:
		pokedata += str(d) + ":"
	return pokedata 


@app.route('/')
def index():
	a = np.array([1, 2, 3, 4])
	b = np.array([1, 2, 3, 4])
	result = a*b
	return render_template('index.html', message=result)

@app.route('/post_request', methods=['POST'])
def post_requwst():
	pokemon1 = request.form["pokemon1"]
	pokemon2 = request.form["pokemon2"]
	pokemon3 = request.form["pokemon3"]
	pokemon4 = request.form["pokemon4"]
	pokemon5 = request.form["pokemon5"]
	pokemon6 = request.form["pokemon6"]
	typelist = list()
	print(pokemon6=="")
	con = sqlite3.connect('test.sqlite3')
	cur = con.cursor()
	pokedata = ""
	cur.execute("select * from t_poke where name like ? or name like ? or name like ? or name like ? or name like ? or name like ?", (pokemon1,pokemon2,pokemon3,pokemon4,pokemon5,pokemon6))
	firstresult = cur.fetchall()
	for row in firstresult:
		pokedata += addstr(row) + "<br>\n"
		typelist += [row[2]]

	lastresult = typechart.partySuggest(typelist)
	print("lastresult")
	print(lastresult)
	print(typelist)
	cur.execute("select * from t_poke where type glob ? and type glob '??' and not type glob'*[" + "".join(typelist) + "]*' order by total desc limit 10", ('*['+"".join(lastresult)+']*',))
	print("".join(lastresult))
	print(cur.fetchall())
	


	cur.close()
	return render_template('index.html', message="calcresult") + pokedata



if __name__ == "__main__":
	app.run(debug=True)
