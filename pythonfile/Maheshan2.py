x=0
while True:
    try:
        x=int(input('Enter your age : '))
        break
    except ValueError as e:
        print(e)
        print('try again')
print(x)