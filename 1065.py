


def checkNum(n):
	a=str(n)
	size=len(a)
	base=int(a[0])-int(a[1])
	result=True		
	i=0
	while i<size-1:
		if base!=(int(a[i])-int(a[i+1])):
			result=False		
		i=i+1
	return result



a=int(raw_input())

if a<100:
	print a
elif a>99:
	count=99
	for i in range(100,a+1):
		if checkNum(i)==True:
			count=count+1
	print count
	
