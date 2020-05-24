from collections import Counter
showList=[]
p=int(input())
showList=list(map(int,input().split()))

dic=Counter(showList)
x=int(input())
sum=0
for i in range(x):
    lst=list(map(int,input().split()))
    if(dic[lst[0]]>0):
        sum=sum+lst[1]
        dic[lst[0]]-=1
print(sum)











'''
lst=[2, 3, 4, 5, 6, 8, 7, 6, 5, 18]
dic=Counter(lst)
print(dic)
dic[5]-=1
dic[5]-=1
print(dic)
'''