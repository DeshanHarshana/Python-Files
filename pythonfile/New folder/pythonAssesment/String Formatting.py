def printFormat(number):
    length=len(bin(number).replace("0b", ""))
    for i in range(1,number+1):
        print(str(i).ljust(length,' '),oct(i).replace("0o", "").ljust(length,' '),hex(i).replace("0x", "").ljust(length,' ').upper(),bin(i).replace("0b", "").ljust(length,' '))

num=int(input())
printFormat(num)