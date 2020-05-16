def checkDuplicateAvailable(lst):
    isDuplicate=False;
    for i in lst:
        if(lst.count(i)>1):
            isDuplicate=True
            break;
    return isDuplicate


lst=[2,3,3,3,4,1,4,6,6]
print(checkDuplicateAvailable(lst))


def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 

print(Repeat(lst))

def remove_dup1(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    return unique_list

lst=[2,3,3,3,3,3,4,5]
print(remove_dup1(lst))

def remove_dup2(x):
      return list(dict.fromkeys(x))
print(remove_dup2(lst))

lst=[1,2,2,3,4,4]
def findNonDups(lst):
    nondup=[]
    for i in lst:
        if(lst.count(i)>1):
            continue;
        else: 
            nondup.append(i)
    return nondup
print(findNonDups(lst))
