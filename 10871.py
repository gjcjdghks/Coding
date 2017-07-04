a=raw_input()
b=a.split()

N=int(b[0])
X=int(b[1])

Num1=raw_input()
Num2=Num1.split()

arr=[]

for x in Num2:
	arr.append(int(x))

output=''
for x in arr:
	if X>x:
		output=output+str(x)+' '


print output



