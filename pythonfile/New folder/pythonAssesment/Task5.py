n = int(input("Enter SIze : "))
m = int(input("Enter Shift size : "))
for i in range(1, n+1):
    for x in range(m):
        print(" ", end='')
    for j in range(1, (n-i)+1):
        print(' ', end='')
    for k in range(0, 2*i-1):
        print('*', end='')
    print()
for i in range(n, 0, -1):
    for x in range(m):
        print(" ", end='')
    for j in range(1, (n-i)+1):
        print(' ', end='')
    for k in range(0, 2*i-1):
        print('*', end='')
    print()
