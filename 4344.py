import sys

a=int(raw_input())

score=[]

for x in range(a):
	b=raw_input()
	score.append(b)

for x_2 in range(a):
	c=[]
	c=score[x_2].split()
	size=int(c[0])
	NUM=0
	Sum=0
	for x_1 in range(1,size+1):
		Sum+=int(c[x_1])

	result= float(Sum)/float(size)

	for x_3 in range(1,size+1):
		if result < int(c[x_3]):
			NUM=NUM+1
	
	sys.stdout.write("%0.3f"%round(float(NUM)/float(size)*100,3))
	print ("%")
	
	

	
	


