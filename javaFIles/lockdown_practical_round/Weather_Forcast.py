t = list(map(int, input().rstrip().split()))
f = list(map(int, input().rstrip().split()))
sum=0
for i in range(len(t)):
    sum=sum+abs((t[i]-f[i]))
print(sum)