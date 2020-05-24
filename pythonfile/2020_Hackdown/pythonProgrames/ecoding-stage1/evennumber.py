i=int(input())
j=int(input())
count=0
for x in range(i,j+1):
    if(x%2==0):
        count+=1
print(count)