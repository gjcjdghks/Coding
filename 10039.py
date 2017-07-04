arr=[0 for x in range(5)]

for x in range(5):
	arr[x]=int(raw_input())
	if arr[x]<40:
		arr[x]=40


print sum(arr)/5

