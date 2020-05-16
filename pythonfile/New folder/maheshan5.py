rows=int(input())
lst=[]
for i in range(rows):
    lst1=list(map(int,input().split()))
    lst.append(lst1)
print(lst)
for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j], end = " ")
    print()