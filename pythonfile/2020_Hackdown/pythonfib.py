
def fib(n):
    if arr[n] != 0:
        return arr[n]
    else:
        arr[n] = fib(n-1) + fib(n-2)
        return arr[n]
arr=[]
arr[0] = 1
arr[1] = 1
print(fib(5))