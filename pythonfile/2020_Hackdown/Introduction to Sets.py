def average(array):
    st=set(array)
    sum=0
    for i in st:
        sum=sum+i
    return (sum/len(st))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)