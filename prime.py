#prime no

num=int(input("enter a number")) 

for i in range(2,num):
	if num%i==0:
		print("not prime")
		break
	elif(i==(num-1)):
		print("prime")

