testcase=int(raw_input())

arr=[[] for i in range(testcase)]

for x in range(testcase):
	arr[x].append(raw_input())

score=1

result=[0 for i in range(testcase)]

for x in range(testcase):
	for y in range(len(arr[x][0])):
		if 'O'==arr[x][0][y]:
			result[x]+=score
			score+=1
		elif 'X'==arr[x][0][y]:
			score=1
	score=1

for x in range(testcase):
	print result[x]
