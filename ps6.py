bookstore = {"New Arrivals":{"COOKING":["Everyday Italian","Giada De Laurentiis","2005","30.00"],"CHILDREN":["Harry Potter","J K.Rowling","2005","29.99"],"WEB":["Learning XML","Erik T. Ray","2003","39.95"]}}
print ("\n\nBOOKSTORE\n\n")
for dic1 in bookstore.values():
	for lst in dic1.values():
		str=str(lst)
		str=str[1:len(str)-1]		
		print (str)
    
