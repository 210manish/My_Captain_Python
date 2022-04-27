def most_frequent(string):
	di={}
	for key in string:
		if key not in di:
			di[key] = 1
		else:
			di[key]+=1
	return di
string=input("Enter a word ")
di=most_frequent(string)
print("The frequency of letters in the given word is:",di)