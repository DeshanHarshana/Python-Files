height=input()
width=input()
num=[]
for i in range(int(height)):
    lst=[]
    for j in range(int(width)):
        lst.append(int(input()))
    num.append(lst)


for k in num:
    print(int(bin(k[0])[2:]), int(oct(k[1])[2:]), (hex(k[2])[2:]))
