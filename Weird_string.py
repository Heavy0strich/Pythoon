def to_weird_case(string):
	dummy= ""
	count = 0
	for i in string:
		if i == " ":
			count = 0
			dummy = dummy + i
		elif count%2 == 0:
			dummy = dummy + i.upper()
			count += 1
		else:
			dummy = dummy + i.lower()
			count += 1
			
	return dummy
	
string = input("Enter a string: ")
print(to_weird_case(string))
	
