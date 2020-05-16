alp = ['n', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = int(input())
rownum = 0
if(num == 1):
    rownum = 1
if(num == 2):
    rownum = 5
if(num > 2):
    rownum = num*3+(num-3)
if(num > 26):
    exit()
for i in range(1, num+1):
    string = ''
    t = 0
    findex = 0
    for j in range(2*i-1):
        if(t >= i):
            findex = i
            break
        string = string+alp[num-j]
        t = t+1

    lst1 = list(string)

    lst1.reverse()

    lst1.pop(0)

    lst = list(string)

    for x in lst1:
        lst.append(x)

    x = ''
    for i in lst:
        x = x+str(i)+'-'
    x = x.strip('-')
    print(x.center(rownum, '-'))

for i in range(num-1, 0, -1):
    string = ''
    t = 0
    findex = 0
    for j in range(2*i-1):
        if(t >= i):
            findex = i
            break
        string = string+alp[num-j]
        t = t+1

    lst1 = list(string)

    lst1.reverse()

    lst1.pop(0)

    lst = list(string)

    for x in lst1:
        lst.append(x)

    x = ''
    for i in lst:
        x = x+str(i)+'-'
    x = x.strip('-')
    print(x.center(rownum, '-'))
