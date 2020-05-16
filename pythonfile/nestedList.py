if __name__ == '__main__':
    lst=[]
    marklist=[]
    for i in range(int(input())):
        for i in range(1):
            x=input()
            y=float(input())
            marklist.append(y)
            sublist=[x,y]
            lst.append(sublist)
    def removeDuplicate(lst):
        # using naive method 
        # to remove duplicated  
        # from list  
        res = [] 
        for i in lst: 
            if i not in res: 
                res.append(i) 
        return res
    newmarklist=removeDuplicate(marklist)
    newmarklist.sort()
    namelist=[]
    for i in lst:
        if(i[1]==newmarklist[1]):
            namelist.append(i[0])
    namelist.sort()
    print(*namelist, sep = "\n")



    