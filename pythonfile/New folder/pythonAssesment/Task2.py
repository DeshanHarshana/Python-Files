n = int(input("Enter SIze : "))
if n > 2:
    for i in range(0, n):
        if(i == 0):
            for j in range(n):
                print('*', end='')
            print()
        if(i > 1 & i < n-2):
            print('*', end='')
            for j in range(0, n-2):
                print('.', end='')
            print('*')
        if(i == n-1):
            for j in range(n):
                print('*', end='')
