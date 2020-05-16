ls =  [12, 24, 1, 2, 23, 3, 22, 4, 21, 20, 5, 19, 6, 7, 18, 17, 8, 9, 16,10]
#this is the list we want to divide two parts
ln=len(ls)
i, j= 0,ln-1

while i < j:
    while (ls[i] > 10): # left part numbers which are > 10
        i += 1
    while (ls[j] <=10): # right part numbers which are <= 10
        j -= 1
    if i < j:
        ls[i], ls[j] = ls[j], ls[i]

print(ls)
