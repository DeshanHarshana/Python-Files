r1=float(input())
r2=float(input())
v=float(input())

bv=v*(5/(5+r1+r2))

if(bv>=5):
    print('Bulb => ON')
else:
    print('Bulb => OFF')