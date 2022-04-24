def printValues():
	l = list()
	for i in [5,10,15,20,25,30]:
		l.append(i)
	lst = (l[0:1])+(l[-1:])
	print(lst)
printValues()