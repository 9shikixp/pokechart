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
	for m in stronglist:
		# print(typeconjap(Type(m).name))
		sugtype += typeconjap(Type(m).name);
	return sugtype

def partySuggest(typelist):
	print(typelist)
	result = np.ones(18)
	for tl in typelist:
		type1 = typeconeng(tl[0])
		calc1 = typechart[:, Type[type1].value]

		if len(tl) == 2:
			type2 = typeconeng(tl[1])
			calc2 = typechart[:, Type[type2].value]
			result *= calc1 * calc2
		else:
			result *= calc1
		print(result)
	print(len(typelist))
	print(result)
	maxweektype = np.where(np.max(result) == result)[0]
	deftypecount = np.zeros(18)
	for mw in maxweektype:
		print(typeconjap(Type(mw).name))
		print("MAX_WEEK_TYPE : " + Type(mw).name);
		tmp = typechart[mw, :]
		stronglist = (np.where(tmp < threshold)[0])
		print("STRONG_TYPE : ")
		for s in stronglist:
			deftypecount[s] += 1
			print(typeconjap(Type(s).name));
		print("-----")


	maxstrong = np.where(np.max(deftypecount) == deftypecount)[0]
	print("MAX_STRONG_TYPE : ")
	sugtype = list()
	for m in maxstrong:
		print(typeconjap(Type(m).name))
		sugtype += typeconjap(Type(m).name);
	
	return sugtype
def partySuggest2(typelist):
	print("typelist")
	print(typelist)
	result = np.zeros(18)
	for tl in typelist:
		atktype = attackSuggest(tl)
		print("atktype: ",atktype)
		for a in atktype:
			result[Type[typeconeng(a)].value] += 1

		deftype = defenceSuggest(tl)
		print("deftype: ",deftype)
		for d in deftype:
			result[Type[typeconeng(d)].value] +=1
	for tl in typelist:
		result[Type[typeconeng(tl[0])].value] = 0
		try:
			result[Type[typeconeng(tl[1])].value] = 0
		except Exception as e:
			print(e)
			print(tl)


	maxstrong = np.where(np.max(result) == result)[0]
	print("result: ",result)
	print("partystrong")
	print(maxstrong)
	sugtype = list()
	for m in maxstrong:
		print(typeconjap(Type(m).name))
		sugtype += typeconjap(Type(m).name);
	
	return sugtype