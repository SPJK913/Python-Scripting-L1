def nonsimilar(lst):
	index=0
	next=index+1
	tmplst=lst
	l=len(tmplst)
	finalLst=[]
	maxI=len(tmplst)-1

	for i,v in enumerate(tmplst):
		next=i+1
		if next>maxI:
			finalLst.append(v)
			break

		if v != tmplst[next]:
			finalLst.append(v)
		
	return finalLst

lst=[2,3,4,3,3,3,2]
lst1=[1, 2, 2, 3]
lst2=[2, 2, 3, 3, 3]

print (lst,nonsimilar(lst),"\n")
print (lst1,nonsimilar(lst1),"\n")
print (lst2,nonsimilar(lst2),"\n")
