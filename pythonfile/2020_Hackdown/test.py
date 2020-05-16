alp = ['n', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
       'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = 3
for i in range(1, num+1):
    string = ''
    t = 0
    for j in range(2*i-1):
        if(t == i):
            break

        string = string+alp[num-t]
        t = t+1
    for k in range(num, i):

        string = string+alp[k-num]
    lst = list(string)

    print(lst)
