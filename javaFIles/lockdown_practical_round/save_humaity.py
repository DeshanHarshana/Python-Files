lst = list(map(int, input().split()))
minus = False
for i in range(len(lst)):
    if(lst[i] <= 0):
        minus = True
        break
sumlist = []
total = 0
for i in lst:
    total = total+i
if((len(lst) <= 1000) & (minus == False)):
    if(len(lst) > 3):
        for i in range(0, len(lst)):
            for j in range(i, len(lst)):
                for k in range(0, len(lst)):
                    if((j != k) & (k != i) & (i != j)):
                        sumlist.append(total-(lst[j]+lst[k]+lst[i]))
    elif(len(lst) <= 3):
        sumlist.append(0)
    elif(len(lst) <= 0):
        exit()
else:
    exit()

sumlist.sort()
print(sumlist[len(sumlist)-1])
