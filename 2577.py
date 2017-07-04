A=int(raw_input())
B=int(raw_input())
C=int(raw_input())

result=A*B*C

arr=[0 for i in range(10)]

while result:
	arr[result%10]+=1
	result/=10

for x in range(10):
	print arr[x]
