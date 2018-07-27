list_1=[]
a=int(input())
for i in range(a):
    a,b=map(int,input().split())
    list_1.append((a,b))
list_1=sorted(list_1,key=lambda X:X[0])
list_1=sorted(list_1,key=lambda X:X[1])
count=0
test=list_1[0][0]
for i in list_1:
    if i[0]>=test:
        test=i[1]
        count+=1
print(count)


