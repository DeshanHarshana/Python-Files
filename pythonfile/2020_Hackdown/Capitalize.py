import math
import os
import random
import re
import sys

def solve(s): 
    namelst=list(map(str,s.split(' ')))

    final_name=''
    for i in namelst:
        fletter=str(i[0])
        name=[]
        if(fletter.isalpha()):
            fletter=fletter.upper()
            
        for x in range(1,len(i)):
            name.append(i[x])
        name.insert(0,fletter)
        
        final_name+=''.join(map(str, name))
        final_name=final_name+" "
    return final_name
if __name__ == '__main__':
    

    s = input()

    result = solve(s)
    print(result)
   

    