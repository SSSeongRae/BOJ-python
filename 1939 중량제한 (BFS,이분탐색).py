##pass


def bfs(m):
    global conn, start, end, visit
    l_2=conn[start][:]
    for i in l_2:
        ##print(" l_2 = ",l_2," m = ",m)
        if i[0]==end and i[1]>=m:
            ##print(3)
            return 1
        elif i[1]>=m and visit[i[0]]!=1:
            visit[i[0]]=1
            for ii in conn[i[0]]:
                if visit[ii[0]]==0:
                    l_2.append(ii)
    ##print(4)
    return 0

N,M=map(int,input().split())
conn=[[] for i in range(100001)]

for i in range(M):
    A,B,C=map(int,input().split())
    conn[A].append([B,C])
    conn[B].append([A,C])
start,end=map(int,input().split())
left=1
right=1000000000

while left<=right:
    visit = [0] * 100001
    mid=int((left+right)/2)
    if bfs(mid):
        left=mid+1
    else:
        right=mid-1
    ##print(" left = ",left, " mid = ",mid ," right = ", right)
print(right)
                  ## 할수잇다 -> 값이 더커져도된다
                 #### 할수없다 -> 값이 작아져야한다




















