n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
print(b)
ans=0
for i in range(n):
    if(a[i]!=b[i]):
        ans+=1
print(ans)
if(ans!=2 and ans!=0):
    print(-1)
elif(ans==0):
    print(0)
else:
    print(1)