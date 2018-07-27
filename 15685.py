## 드래곤커브 삼성 SW 테스트

##  x + 1  -> y + 1
##  x - 1  -> y - 1
##  y + 1  -> x - 1
##  y - 1  -> x + 1

def dra(A, B):
    global point_set, d, g, count, l_3
    ##print(A,B)
    l_1 = B[:]
    if count == g + 1:
        for ii in B:
            l_3[ii[0]][ii[1]] = 1
        ##print("finish")
        return
    if count == 0:
        if d == 0:
            l_1.append([x + 1, y])
        if d == 1:
            l_1.append([x, y - 1])
        if d == 2:
            l_1.append([x - 1, y])
        if d == 3:
            l_1.append([x, y + 1])
        count += 1
        dra(l_1[-1], l_1)
    else:
        l_2 = []
        end = l_1[-1]
        ##print("end",end)
        l_1.reverse()
        for i in range(len(l_1) - 1):
            ##print(l_1[i][0],l_1[i+1][0])
            if l_1[i][0] - l_1[i + 1][0] == -1:
                l_2.append([end[0], end[1] + 1])
            elif l_1[i][0] - l_1[i + 1][0] == 1:
                l_2.append([end[0], end[1] - 1])
            elif l_1[i][1] - l_1[i + 1][1] == -1:
                l_2.append([end[0] - 1, end[1]])
            elif l_1[i][1] - l_1[i + 1][1] == 1:
                l_2.append([end[0] + 1, end[1]])
            end = l_2[-1]
        l_1.reverse()
        l_1 = l_1 + l_2
        count += 1
        ##print(l_1)
        dra(l_1[-1], l_1)


N = int(input())
l_3 = [[0] * 101 for i in range(101)]
for i in range(N):
    count = 0
    x, y, d, g = map(int, input().split())
    dra([x, y], [[x, y]])

count = 0

for ii in range(100):
    for jj in range(100):
        if l_3[ii][jj] == 1 and l_3[ii + 1][jj] == 1 and l_3[ii][jj + 1] and l_3[ii + 1][jj + 1]:
            count += 1
print(count)
