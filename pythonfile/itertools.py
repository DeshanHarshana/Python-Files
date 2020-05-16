from itertools import product

lst1=list(map(int,input().split()))
lst2=list(map(int,input().split()))

lst=list(product(lst1,lst2))
string=''
for i in range(len(lst)):
    string=string+'('
    for j in range(len(lst[0])):
        if(j==len(lst[0])-1):
            string=string+' '+str(lst[i][j])
        else:
            string=string+str(lst[i][j]) + ','
    if(i==len(lst)-1):
        string=string+') '
    else:
        string=string+') '

print(string)






'''
lst=list(product([1,2],repeat =1)) #make list that one group has three members and write 
                                    #groups that containt diffrent form others
                                    #actualy cartisiyan product
print(lst)

lst=list(product([1,2,3],[3,4,5]))
print(lst)

A = [[1,2,3],[3,4,5]]
lst=list(product(*A))
print(lst)
B = [[1,2,3],[3,4,5],[7,8]]
lst=list(product(*B))
print(lst)
'''