n=1
m=0
l=int(input("Enter a number "))
for i in range(l):
	if i==0:
		print(m,end=" ")
	elif i==1:
		print(n,end=" ")
	else:
		n+=m
		m=n-m
		print(n,end=" ")