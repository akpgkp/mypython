#prime list

num=int(input("enter a number")) 

for j in range(2,num+1):
	for i in range(2,j):
		if j%i==0:
			#print("not prime")
			break
	else:
		print(j, end=" ")

