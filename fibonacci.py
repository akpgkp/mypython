#fibonacci series 0 1 1 2 3 5 8 13 21...

a=0
print(a, end=",")
b=1
print(b,end=",")

sum=0
for i in range(3,11):
	sum=a+b
	print(sum,end=",")
	a=b
	b=sum

