a=raw_input()

b=a.split()
N=int(b[0])

Num1=raw_input()
Num2=Num1.split()

arr=[]

for x in Num2:
	arr.append(int(x))

Max=max(arr)

arr2=[]

for x in arr:
	arr2.append(float(x)/float(Max)*100)

result=sum(arr2)/N

print round(result,2)



