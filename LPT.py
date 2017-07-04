# -*- coding: utf-8 -*- 


def test(inlist,com):
	outlist=[]
	sumout=[]

	for num in range(com):
		outlist.append([])
		sumout.append(0)

	inlist.sort(reverse=True)

	for x in inlist:
		lowbox=sumout.index(min(sumout))
		outlist[lowbox].append(x)
		sumout[lowbox]+=x

	return outlist

a=raw_input('computer : ')
b=raw_input('program : ')

blist=[]
blist=b.split(' ')
clist=[]
for s in blist:
	clist.append(int(s))

print (test(clist,int(a)))
