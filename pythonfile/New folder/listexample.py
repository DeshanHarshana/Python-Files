lt=[]
def command(lst):
    if lst[0] == 'insert':
        lt.insert(int(lst[1]), int(lst[2]))
    elif lst[0] == 'remove':
        lt.remove(int(lst[1]))
    elif lst[0] == 'append':
        lt.append(int(lst[1]))
    elif lst[0] == 'sort':
        lt.sort()
    elif lst[0] == 'print':
        print(lt)
    elif lst[0] == 'pop':
        lt.pop()
    elif lst[0] == 'reverse':
        lt.reverse()

count=int(input())
print(count)
for i in range(count):
    inputvalue=input().split()
    command(inputvalue)

