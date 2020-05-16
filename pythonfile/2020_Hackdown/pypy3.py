import re
import math
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 
    
    # n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
    # is a perferct square 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
     
# A utility function to test above functions 


n=int(input())
lst=""
for i in range(n):
    lst=lst+input()

numbers=list(re.findall(r'\d+', lst))
lst2=[]

for i in numbers:
    if(isFibonacci(int(i))):
        lst2.append(i)
lst2.sort()

print(lst2[0])