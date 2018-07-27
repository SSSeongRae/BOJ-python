import math

def check(time):
    global l_1
    A=0
    for i in range(len(l_1)):
        A+=math.ceil(time/l_1[i])
    return A


N,M=map(int,input().split())
l_1=list(map(int,input().split()))
left=1
right=60000000000
while(left<=right):
    mid=((left+right)//2)
    ck=check(mid)
    if ck>=N:
        right=mid-1
    else:
        left=mid+1
    ##print(ck,mid,left,right)

a_1=N-check(right)
l_2=[]
for i in range(len(l_1)):
    if (right)%l_1[i]==0:
        l_2.append(i)

l_2.sort()
##print(l_2)
print(l_2[a_1-1]+1)

