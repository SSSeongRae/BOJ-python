import collections

N,K=map(int,input().split())
l_1=collections.deque([[N,0]])
visit=[0]*100001
while(l_1):
    A=l_1.popleft()
    visit[A[0]]=1
    if A[0]==K:
        print(A[1])
        break
    else:
        if not A[0]-1<0 and not visit[A[0]-1] == 1 :
            l_1.append([A[0]-1,A[1]+1])
        if A[0]+1<=100000:
            if not visit[A[0]+1] == 1:
                l_1.append([A[0]+1,A[1]+1])
        if A[0]*2<=100000:
            if not visit[A[0]*2] ==1:
                l_1.append([A[0]*2,A[1]+1])
