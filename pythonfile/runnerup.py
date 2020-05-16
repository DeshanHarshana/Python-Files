n = int(input())
arr = map(int, input().split())
lst=list(arr)
res = [] 
for i in lst: # REMOVE DUPLICATE VALUES
    if i not in res: 
        res.append(i)
res.sort()

print(res[len(res)-2])