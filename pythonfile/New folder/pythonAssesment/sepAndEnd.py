lst=[1,2,3,4]
print(lst,end='\n')#print new line after list print
print('1','2','3',sep=":")#1:2:3
print('1','2','3',end=":")#1 2 3:
print()
for i in lst:
    print(i,sep=":")#we can't sep because one time come one value
    #then how we seprte value

for i in lst:
    print(i,end=":")#1:2:3:4: