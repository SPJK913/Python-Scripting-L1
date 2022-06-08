list1=['axa', 'xyz', 'gg', 'x', 'yyy']
list2=['x', 'cd', 'cnc', 'kk']
list3=['bab', 'ce', 'cba', 'syanora']
def StringCount(tlist):
	sCount=0
	for ele in tlist:
		if ( len(ele)>=2 ) and ( ele[0] == ele[-1] ):
			sCount+=1
	return sCount

print StringCount(list1)
print StringCount(list2)
print StringCount(list3)
