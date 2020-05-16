import random

ls =  [12, 24, 1, 2, 23, 3, 22, 4, 21, 20, 5, 19, 6, 7, 18, 17, 8, 9, 16]
ls = [22, 5, 93, 5, 7, 99, 1, 18, 58, 1, 8, 90]
ls = [5, 1, 9, 2, 8, 3, 7, 5, 6, 4]
ls = [random.randint(1,100) for i in range(20)]

print(ls)
ln = len(ls)
p = ls[0]
i=0 
j =ln-1

while i < j :
    while ls[i] <= p :
        i += 1

    while ls[j] >= p:
        j -= 1

    if i < j:
        ls[i], ls[j] = ls[j], ls[i]


print(ls)

# this code divide given list to two part 
# put numbers which are less than or equal to 0th index number to left side
# put numbers which are greater than or equal to 0th index number to right side
# we can use this code for divide given array according to some condition