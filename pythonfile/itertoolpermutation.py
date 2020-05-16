from itertools import permutations
from operator import itemgetter
r=list(map(str,input().split()))
lst=list(permutations(r[0],int(r[1])))




lst1=[]
for i in range(len(lst)):
    s=""
    for j in range(len(lst[0])):
        s=s+str(lst[i][j])
    lst1.append(s)
b_list = sorted(lst1, key=str.lower)
for i in b_list:
    print(i)
'''
lst=list(permutations(['x','x','x']))
print(lst)
lst=list(permutations(['1','2','3'],2))
print(lst)
'''