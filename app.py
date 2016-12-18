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
	pokemon = list()
	pokemon += ["","","","","",""]
	return render_template('index.html', message="パーティ補完ツール", pokemon=pokemon)

@app.route('/post_request', methods=['POST'])
def post_requwst():
	pokemon = list()
	for x in range(1,7):
		pokemon += [request.form["pokemon"+str(x)]]
	typelist = list()
	print(pokemon[5]=="")
	con = sqlite3.connect('test.sqlite3')
	cur = con.cursor()
	# pokedata = ""
	cur.execute("select * from t_poke where name like ? or name like ? or name like ? or name like ? or name like ? or name like ?", (pokemon[0],pokemon[1],pokemon[2],pokemon[3],pokemon[4],pokemon[5]))
	firstresult = cur.fetchall()
	for row in firstresult:
		# pokedata += addstr(row) + "<br>\n"
		typelist += [row[2]]

	atkresult, defresult = typechart.partySuggest(typelist)
	# print("atkresult")
	# print(atkresult)
	# print(typelist)
	cur.execute("select * from t_poke where type glob ? and type glob ? and type glob '??' order by total desc limit 10", ('*['+"".join(atkresult)+']*','*['+"".join(defresult)+']*'))
	# and not type glob'*[" + "".join(typelist) + "]*'
	print("atkresult","".join(atkresult))
	print("defresult","".join(defresult))
	sugtype = "攻撃側のおすすめ:" + "".join(atkresult) + "<br>\n防御側のおすすめ:" + "".join(defresult) + "\n"
	suggestResult = cur.fetchall()
	print(len(suggestResult)==0)
	if len(suggestResult)==0:
		cur.execute("select * from t_poke where (type glob ? or type glob ?) and type glob '??'  order by total desc limit 10", ('*['+"".join(atkresult)+']*','*['+"".join(defresult)+']*'))
		# and not type glob'*[" + "".join(typelist) + "]*'
		suggestResult = cur.fetchall()
	print(suggestResult)

	sugpoke = "<hr>\nおすすめのポケモン<br>\n"
	for row in suggestResult:
		sugpoke += row[1] + ":" + row[2] + "<br>\n"
	
	print("pokemon: ", pokemon)


	cur.close()
	return render_template('index.html', message="計算結果", pokemon=pokemon) + sugtype + sugpoke

if __name__ == "__main__":
	app.run(debug=True)
