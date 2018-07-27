## pass
def A(x,y,l):
    global check, count
    if check:
        return
    if c<=x+l-1 and r<=y+l-1:
        l_1=[]
        if x==c and y==r:
            print(int(count))
            check=1
            return
        elif l==1:
            count+=1
            return
        else:
            l_1.append([x,y,l/2])
            l_1.append([x+l/2,y,l/2])
            l_1.append([x,y+l/2,l/2])
            l_1.append([x+l/2,y+l/2,l/2])
            for i in l_1:
                A(i[0],i[1],i[2])
    else:
        count+=l**2


check=0
N,r,c=map(int,input().split())
count=0
A(0,0,2**N)

## 시작점 , 길이
