n=10
for i in range(n):
    if(i==0 or i==n-1):
        print('*'*n, end='\n')
    
    else:
        print('*', '.'*(n-2), '*', sep='')
    
   