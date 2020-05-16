s1='Cat'
s2='tac'
isAnaggram=False;
if(len(s1)==len(s2)):
    for i in range(0,len(s1)-1):
        if(s1.count(s2[i].lower())==s2.count(s2[i].lower())):
            isAnaggram=True
        else:
            isAnaggram=False
print(isAnaggram)