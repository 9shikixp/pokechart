import numpy as np
from enum import Enum
class Type(Enum):
	normal = 0
	fire = 1
	water = 2
	electric = 3
	grass = 4
	ice = 5
	fighting = 6
	poison = 7
	ground = 8
	flying = 9
	psychic = 10
	bug = 11
	rock = 12
	ghost = 13
	dragon = 14
	dark = 15
	steel = 16
	fairy = 17

typetoeng = {'無': 'normal', '炎': 'fire', '水': 'water',
			 '電':'electric', '草': 'grass', '氷': 'ice',
			 '闘': 'fighting', '毒': 'poison', '地':'ground', 
			 '飛': 'flying', '超': 'psychic', '虫': 'bug', 
			 '岩': 'rock', '霊': 'ghost', '竜': 'dragon', 
			 '悪': 'dark', '鋼': 'steel', '妖': 'fairy'}
typetojap = {'normal': '無', 'fire': '炎', 'water': '水',
			 'electric': '電', 'grass': '草', 'ice': '氷',
			 'fighting': '闘', 'poison': '毒', 'ground': '地', 
			 'flying': '飛', 'psychic': '超', 'bug': '虫', 
			 'rock': '岩', 'ghost': '霊', 'dragon': '竜', 
			 'dark': '悪', 'steel': '鋼', 'fairy': '妖'}

typechart = np.array(
	[[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,0.5,  0,  1,  1,0.5,  1],
	[  1,0.5,0.5,  1,  2,  2,  1,  1,  1,  1,  1,  2,0.5,  1,0.5,  1,  2,  1],
	[  1,  2,0.5,  1,0.5,  1,  1,  1,  2,  1,  1,  1,  2,  1,0.5,  1,  1,  1],
	[  1,  1,  2,0.5,0.5,  1,  1,  1,  0,  2,  1,  1,  1,  1,0.5,  1,  1,  1],
	[  1,0.5,  2,  1,0.5,  1,  1,0.5,  2,0.5,  1,0.5,  2,  1,0.5,  1,0.5,  1],
	[  1,0.5,0.5,  1,  2,0.5,  1,  1,  2,  2,  1,  1,  1,  1,  2,  1,0.5,  1],
	[  2,  1,  1,  1,  1,  2,  1,0.5,  1,0.5,0.5,0.5,  2,  0,  1,  2,  2,0.5],
	[  1,  1,  1,  1,  2,  1,  1,0.5,0.5,  1,  1,  1,0.5,0.5,  1,  1,  0,  2],
	[  1,  2,  1,  2,0.5,  1,  1,  2,  1,  0,  1,0.5,  2,  1,  1,  1,  2,  1],
	[  1,  1,  1,0.5,  2,  1,  2,  1,  1,  1,  1,  2,0.5,  1,  1,  1,0.5,  1],
	[  1,  1,  1,  1,  1,  1,  2,  2,  1,  1,0.5,  1,  1,  1,  1,  0,0.5,  1],
	[  1,0.5,  1,  1,  2,  1,0.5,0.5,  1,0.5,  2,  1,  1,0.5,  1,  2,0.5,0.5],
	[  1,  2,  1,  1,  1,  2,0.5,  1,0.5,  2,  1,  2,  1,  1,  1,  1,0.5,  1],
	[  0,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,  1,  2,  1,0.5,  1,  1],
	[  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  1,0.5,  0],
	[  1,  1,  1,  1,  1,  1,0.5,  1,  1,  1,  2,  1,  1,  2,  1,0.5,  1,0.5],
	[  1,0.5,0.5,0.5,  1,  2,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,0.5,  2],
	[  1,0.5,  1,  1,  1,  1,  2,0.5,  1,  1,  1,  1,  1,  1,  2,  2,0.5,  1]])

threshold = np.ones(18)

def typeconeng(typejap):
	return typetoeng[typejap]
def typeconjap(typeeng):
	return typetojap[typeeng]

def attackSuggest(poketype):
	print("atk_poketype: ", len(poketype))
	type1 = typeconeng(poketype[0])
	calc1 = typechart[Type[type1].value, :]

	if len(poketype) == 2:
		type2 = typeconeng(poketype[1])
		calc2 = typechart[Type[type2].value, :]
		result = np.maximum(calc1,calc2)
	else:
		result = calc1
	# print("result: ",result)

	typecount = np.zeros(18)
	weeklist = (np.where(result < threshold)[0])
	for w in weeklist:
		print("WEEK_TYPE : " + Type(w).name);
		tmp = typechart[:, w]
		stronglist = (np.where(tmp > threshold)[0])
		# print("STRONG_TYPE : ")
		for s in stronglist:
			typecount[s] += 1
			# print(typeconjap(Type(s).name));
		# print("-----")
	print(typecount)
	maxstrong = np.where(np.max(typecount) == typecount)[0]
	# print("MAX_STRONG_TYPE : ")
	sugtype = list()
	for m in maxstrong:
		# print(typeconjap(Type(m).name))
		sugtype += typeconjap(Type(m).name);
	return sugtype

def defenceSuggest(poketype):
	type1 = typeconeng(poketype[0])
	calc1 = typechart[:, Type[type1].value]

	if len(poketype) == 2:
		type2 = typeconeng(poketype[1])
		calc2 = typechart[:, Type[type2].value]
		result = calc1 * calc2
	else:
		result = calc1
	# print(result)

	typecount = np.zeros(18)
	weeklist = (np.where(result > threshold)[0])
	for w in weeklist:
		print("WEEK_TYPE : " + Type(w).name);
		tmp = typechart[w, :]
		stronglist = (np.where(tmp < threshold)[0])
		# print("STRONG_TYPE : ")
		for s in stronglist:
			typecount[s] += 1
			# print(typeconjap(Type(s).name));
		# print("-----")
	print(typecount)
	maxstrong = np.where(np.max(typecount) == typecount)[0]
	# print("MAX_STRONG_TYPE : ")
	sugtype = list()
	for m in maxstrong:
		# print(typeconjap(Type(m).name))
		sugtype += typeconjap(Type(m).name);
	return sugtype

def partySuggest(typelist):
	print(typelist)
	atkresult = np.ones(18)
	defresult = np.ones(18)
	stronglist = np.ones(18)

	for tl in typelist:
		type1 = typeconeng(tl[0])

		atkcalc1 = typechart[Type[type1].value, :]

		defcalc1 = typechart[:, Type[type1].value]

		stronglist[Type[type1].value] = 0

		if len(tl) == 2:
			type2 = typeconeng(tl[1])

			atkcalc2 = typechart[Type[type2].value, :]
			atkresult *= np.maximum(atkcalc1,atkcalc2)

			defcalc2 = typechart[:, Type[type2].value]
			defresult *= defcalc1 * defcalc2

			stronglist[Type[type2].value] = 0

		else:
			atkresult *= atkcalc1
			defresult *= defcalc1
	print("atkresult: ", atkresult)
	print("defresult: ", defresult)


	atkweektype = np.where(np.min(atkresult) == atkresult)[0]
	defweektype = np.where(np.max(defresult) == defresult)[0]

	atktypecount = np.zeros(18)
	deftypecount = np.zeros(18)

	for awt in atkweektype:
		print("ATK_WEEK_TYPE : " + Type(awt).name);
		tmp = typechart[:, awt]
		atkstronglist = (np.where(tmp > threshold)[0])
		print("ATK_STRONG_TYPE : ")
		for asl in atkstronglist:
			atktypecount[asl] += 1
			print(typeconjap(Type(asl).name));
	print("-----")

	for dwt in defweektype:
		print("DEF_WEEK_TYPE : " + Type(dwt).name);
		tmp = typechart[dwt, :]
		defstronglist = (np.where(tmp < threshold)[0])
		print("DEF_STRONG_TYPE : ")
		for dsl in defstronglist:
			deftypecount[dsl] += 1
			print(typeconjap(Type(dsl).name));
	print("-----")

	atktypecount *= stronglist
	deftypecount *= stronglist

	# atkmaxstrong = np.where(np.max(atktypecount) == atktypecount)[0]
	# defmaxstrong = np.where(np.ma np.where(np.max(deftypecount) == deftypecount)[0]x(deftypecount) == deftypecount)[0]


	# stronglist *= (atktypecount + deftypecount)


	# maxstrong = np.where(np.max(stronglist) == stronglist)[0]
	# print("MAX_STRONG_TYPE : ")
	# sugtype = list()
	# for m in maxstrong:
	# 	print(typeconjap(Type(m).name))
	# 	sugtype += typeconjap(Type(m).name);
	# return sugtype
	maxatkstrong = np.where(np.max(atktypecount) == atktypecount)[0]
	maxdefstrong = np.where(np.max(deftypecount) == deftypecount)[0]
	print("atktypecount: ",atktypecount)
	print("deftyoecount: ",deftypecount)
	print("partystrong")
	print("mas",maxatkstrong)
	print("mds",maxdefstrong)
	atksugtype = list()
	defsugtype = list()
	for m in maxatkstrong:
		print(typeconjap(Type(m).name))
		atksugtype += typeconjap(Type(m).name);
	for m in maxdefstrong:
		print(typeconjap(Type(m).name))
		defsugtype += typeconjap(Type(m).name);

	return atksugtype, defsugtype

def partySuggest2(typelist):
	print("typelist")
	print(typelist)
	atkresult = np.zeros(18)
	defresult = np.zeros(18)
	for tl in typelist:
		atktype = attackSuggest(tl)
		print("atktype: ",atktype)
		for a in atktype:
			atkresult[Type[typeconeng(a)].value] += 1

		deftype = defenceSuggest(tl)
		print("deftype: ",deftype)
		for d in deftype:
			defresult[Type[typeconeng(d)].value] +=1
	for tl in typelist:
		atkresult[Type[typeconeng(tl[0])].value] = 0
		defresult[Type[typeconeng(tl[0])].value] = 0
		
		try:
			atkresult[Type[typeconeng(tl[1])].value] = 0
			defresult[Type[typeconeng(tl[1])].value] = 0
		except Exception as e:
			print(e)
			print(tl)

	maxatkstrong = np.where(np.max(atkresult) == atkresult)[0]
	maxdefstrong = np.where(np.max(defresult) == defresult)[0]
	print("atkresult: ",atkresult)
	print("defresult: ",defresult)
	print("partystrong")
	print("mas",maxatkstrong)
	print("mds",maxdefstrong)
	atksugtype = list()
	defsugtype = list()
	for m in maxatkstrong:
		print(typeconjap(Type(m).name))
		atksugtype += typeconjap(Type(m).name);
	for m in maxdefstrong:
		print(typeconjap(Type(m).name))
		defsugtype += typeconjap(Type(m).name);

	return atksugtype, defsugtype