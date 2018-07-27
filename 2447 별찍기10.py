def divv(x,y,l):
    global l_1
    if l==1:
        l_1[x][y]="*"
    else:
        divv(x,y,l//3)
        divv(x,y+l//3,l//3)
        divv(x,y+(l//3)*2,l//3)
        divv(x+l//3,y,l//3)
        divv(x+l//3,y+(l//3)*2,l//3)
        divv(x+(l//3)*2,y,l//3)
        divv(x+(l//3)*2,y+l//3,l//3)
        divv(x+(l//3)*2,y+(l//3)*2,l//3)

N=int(input())
l_1=[[" "for i in range(N)] for j in range(N)]

divv(0,0,N)
for ii in range(N):
    print(''.join(l_1[ii]))

# pass



