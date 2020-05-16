def calc(n):
    lst=[]
    i=1
    for i in range(1,n):
        lst.append(i)
    print(*lst, sep = "**")#*lst output list without bracket and commas, sep='' using to remove spaces


calc(20)
