ls =  [12, 24, 1, 2, 23, 3, 22, 4, 21, 20, 5, 19, 6, 7, 18, 17, 8, 9, 16]
#this is the list we want to divide two parts
ln=len(ls)
i, j= 0,ln-1

while i < j:
    while (ls[i] % 2 == 1): # left hand side part. (ls[i]) part is constant and logic is only %2==1
                            # it means put things to left part which are %2==1 is proof
        i += 1
    while (ls[j] % 2 == 0): # right hand side part. (ls[j]) part is constant and logic is only %2==1
                            # it means put things to right part which are %2==0 is proof (even number)
        j -= 1
    if i < j:
        ls[i], ls[j] = ls[j], ls[i]

print(ls)
