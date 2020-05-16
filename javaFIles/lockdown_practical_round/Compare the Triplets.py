a=list(map(int,input().split()))
b=list(map(int,input().split()))
aSum=0;
bSum=0;
for i in range(len(a)):
    if(a[i]>b[i]):
        aSum+=1
    elif(a[i]<b[i]):
        bSum+=1
print(aSum, bSum)