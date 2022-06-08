def customSort(lst):
	tmpList=lst
	Xlst=[];nonXlst=[]
	for n in tmpList:
		if n[0].lower() == "x" :
			Xlst.append(n)
		else:
			nonXlst.append(n)
	Xlst.sort(),nonXlst.sort()
	return Xlst + nonXlst


#main program
lst1=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
lst2=['bbb', 'ccc', 'axx', 'xzz', 'xaa']

print( lst1," is sorted as \n",customSort(lst1),"\n")
print (lst2," is sorted as \n",customSort(lst2),"\n")
