class Question2:
    size = int(input())
    nums = []
    for i in range(size):
        nums.append(int(input()))
    for i in nums:
        sum=0
        for x in range(i):
            if(x%3==0):
                sum=sum+x
            elif(x%5==0):
                sum=sum+x
        print(sum)

