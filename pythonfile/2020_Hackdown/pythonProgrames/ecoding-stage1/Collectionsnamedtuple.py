from collections import namedtuple
n=int(input())
rows=(input().split())

sum=0;
index=0;
for k in range(len(rows)):
    if(rows[k]=="MARKS"):
        index=k

for i in range(n):
    lst=list(map(str,input().split()))
    for j in range(len(lst)):
        if(j==index):
            sum=sum+int(lst[j])
print('%.2f' %(sum/n))


'''
Point = namedtuple('Point','x,y')

pt1 = Point(1,2)
print(pt1.x)
print(pt1.y)
'''