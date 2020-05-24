ls = [2, 4, 6, 8, 10]
print(ls)
ln = len(ls)
i, j = 0, ln-1
while i < j :
    while (ls[i]%2 == 1) : 
        i += 1
    while (ls[j] % 2 == 0):
        j -= 1
    if i < j:
        ls[i], ls[j] = ls[j], ls[i]

print(ls)

# purpose of this code is this code divide given list to two part
# it add odd numbers in given list to left hand side part
# it add even numbers in given list to right hand side part