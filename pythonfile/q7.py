inputs = list(map(str,input().split()))
originalList=[]
coun=inputs.count('ab')
for i in range(6):
    originalList.append(inputs[i])
inputs.sort(reverse=-1)
sortedlist=[]
print(coun)
for i in range(coun):
    inputs.remove('ab')
if coun<3:
    for i in range(3):
        sortedlist.append(inputs[i])
else:
    for i in range(6-coun):
        sortedlist.append(inputs[i])
print(sortedlist)
if coun>3:
    for i in range(coun-3):
        sortedlist.insert(len(sortedlist)+1,'ab')

print(sortedlist)
indexlist=[]
