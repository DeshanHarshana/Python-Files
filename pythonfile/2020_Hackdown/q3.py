lst=list(map(float,input().split()))
print(lst)
x=lst[1]/((1/lst[0])+lst[1]-((1/lst[0])*lst[1]))
print("%.2f" % x)