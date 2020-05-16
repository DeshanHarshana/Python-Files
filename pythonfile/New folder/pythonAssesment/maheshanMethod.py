

def show(a,b,/):
    print(b-a,)
#if we use blackslash after paremeters we can't use folloing way
show(2,5)
#show(b=100, a=454)#show() got some positional-only arguments passed as keyword arguments

def calc(a,b,/,op='+'):#defaulf value = '+'
    res=0
    if op == '+' :
        res = a + b
    elif op == '-' :
        res = a - b
    elif op == '*' :
        res = a * b
    elif op == '/' :
        res = a // b
    elif op == '/':
        res = a/b
    elif op == '**':
        res = a**b
    else:
        print(f"{op} is not implemented") #f-string in Python 3.6.x
        res = None
    return res
print(calc(2,5))#default value = +
print(calc(4,6,'-'))
print(calc(3,6,op='+'))#we can use op because it define after /
#we can't say a=4, b=3

print(calc(4,6,'**'))