import itertools

while(True):
    l_1=list(input().split())
    if l_1[0] =='0':
        break
    else:
        l_2=l_1[1:]
        ##for i in itertools.permutations(1_2,6):
          ##  print(i)
        a=list(map(' '.join, itertools.combinations(l_2,6)))
        for i in a:
            print(i)
        print()

