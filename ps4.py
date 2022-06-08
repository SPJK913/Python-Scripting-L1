def getLastEle(tup):
	return tup[-1]

def customSort(lst):
	tmplst=lst
	tmplst.sort(key=getLastEle)
	return tmplst

lst1=[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
lst2=[(1, 3), (3, 2), (2, 1)]

print (lst1,"\n is sorted as \n",customSort(lst1))
print (lst2,"\n is sorted as \n",customSort(lst2))
