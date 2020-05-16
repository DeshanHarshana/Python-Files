size=25
for i in range(0,size):
    
    for j in range(size-1,i,-1):
        print(' ', end='');
    for k in range(-1,i,1):
        print('* ', end='')
    print()