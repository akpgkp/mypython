#display bytesarray array

elements=[ 50,40,30,20,10]

x= bytearray(elements)

for i in x: print(i)

x[0]=1
x[1]=2

print("modified bytearray")
for i in x: print(i)