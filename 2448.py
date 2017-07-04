import sys

def star(Mat,to):
    Mat[0][to-1]='*'
    Mat[1][to-2]='*'
    Mat[1][to]='*'
    Mat[2][to-3]='*'
    Mat[2][to-2]='*'
    Mat[2][to-1]='*'
    Mat[2][to]='*'
    Mat[2][to+1]='*'
    
def func(Mat,line,here,to):
    saveline=line
    while(here<to):
        i=0
        while(i<here):
            if(Mat[line][to-1+i]=='*'):
                Mat[line+here][to-1-(here)+i]=Mat[line][to-1+i]
                Mat[line+here][to-1+(here)+i]=Mat[line][to-1+i]
                Mat[line+here][to-1-(here)-i]=Mat[line][to-1+i]
                Mat[line+here][to-1+(here)-i]=Mat[line][to-1+i]
            i+=1
        saveline=line+here
        here=here*2
        func(Mat,saveline,here,to)
            
to=int(input())
Mat=[[' ']*(2*to-1) for i in range(to)]
star(Mat,to)
func(Mat,0,3,to)
func(Mat,1,3,to)
func(Mat,2,3,to)

i=0
j=0
here=3
for i in range(to):
    for j in range(to*2-1):
	sys.stdout.write(Mat[i][j])
    print ''
    if( i == (here-1) ):
        here=here*2
