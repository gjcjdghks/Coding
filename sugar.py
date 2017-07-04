FIVE=5
result=0

num=int(raw_input())

if(num%FIVE==0):
	result=(num/FIVE)
elif(num%FIVE ==1):
	result=(num/FIVE)+1
elif(num%FIVE ==2):
	result=-1
	if((num/FIVE)%3==2):
		result=num/3
	if(num>15):
		result=num/FIVE+2
elif(num%FIVE ==3):
	result=(num/FIVE)+1
elif(num%FIVE ==4):
	result=(num/FIVE)+2
	if(num==4):
		result=-1;

print result

