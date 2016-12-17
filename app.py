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
	pokemon = list()
	pokemon += [request.form["pokemon1"]]
	pokemon += [request.form["pokemon2"]]
	pokemon += [request.form["pokemon3"]]
	pokemon += [request.form["pokemon4"]]
	pokemon += [request.form["pokemon5"]]
	pokemon += [request.form["pokemon6"]]

	typelist = list()
	print(pokemon[5]=="")
	con = sqlite3.connect('test.sqlite3')
	cur = con.cursor()
	pokedata = ""
	cur.execute("select * from t_poke where name like ? or name like ? or name like ? or name like ? or name like ? or name like ?", (pokemon[0],pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5]))
	firstresult = cur.fetchall()
	for row in firstresult:
		pokedata += addstr(row) + "<br>\n"
		typelist += [row[2]]

	atkresult, defresult = typechart.partySuggest(typelist)
	# print("atkresult")
	# print(atkresult)
	# print(typelist)
	cur.execute("select * from t_poke where type glob ? and type glob ? and not type glob'*[" + "".join(typelist) + "]*' order by total desc limit 10", ('*['+"".join(atkresult)+']*','*['+"".join(defresult)+']*'))
	print("atkresult","".join(atkresult))
	print("defresult","".join(defresult))
	print(cur.fetchall())
	
	print("pokemon: ", pokemon)

	cur.close()
	return render_template('index.html', message="calcresult", pokemon=pokemon) + pokedata



if __name__ == "__main__":
	app.run(debug=True)
