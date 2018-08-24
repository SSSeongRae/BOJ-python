def check(A):
    global l_1
    for j in str(A):
        if l_1[int(j)]:
            continue
        else:
            return False
    return True


N=int(input())
M=int(input())
l_1=[1]*10
if M:
    ll=map(int,input().split())
    for i in ll:
      l_1[i]=0
min1=abs(N-100)

for i in range(0,1000000):
    if check(i):
        min1=min(min1,abs(N-i)+len(str(i)))

print(min1)

## pass