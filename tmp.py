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