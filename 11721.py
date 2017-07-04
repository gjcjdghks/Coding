a=raw_input()

i=0
b=''
for x in a:
	b+=a[i]
	i=i+1
	if i%10==0:
		b+='\n'

print b
	


