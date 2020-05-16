marks = [56, 45, 87, 30, 95, 39]
for m in marks:
    if m < 40:
        print(m)
        break
print('Done')
#if met break statement it will exit loop
marks = [56, 45, 87, 30, 95, 39]
for m in marks:
    if m < 40:
        print(m)
        continue
print('Done')
#if met continue statement it will go to begining of loop

ls = [13, 6, 92, 99, 22, 6, 1, 9, 43]
for i in ls:
    if i%3:
        continue
#end if
    print(i)
#end for
print('Done')
#let get 13 then 13%3 is 1 1 is a number then it definitly go to inside the if and continue no print 13
#let get 6 then 6%3 is 0 then it is not come inside if and print 6

#for loop with else part
'''
n = 91
primes10 = [2, 3, 5, 7]
for p in primes10:
    if n % p :
        continue
# end if
else:
    print(n, 'is not divisible by any of the prime numbers < 10')
'''
'''
numbers=[1,2,3,4,5,6,7,8,9]
for i in numbers:
    if(i%3==0):
        print(i)
        break
else:
    print('This number list not contain numbers which can divide by 3')
'''
numbers=[1,2,3,4,5,7,8]
for i in numbers:
    if(i%5==0):
        break
    
else:
    print('This number list not contain numbers which can divide by 3')

'''
we can use else keyword with for loop, it will help to find that break keyword execute
if break keyword execute one time then normal for loop exit the loop but we have no way to find whather it meet or not
then we can use else keyword, if we haven't met break keyword it execute else part otherwise not
even if it met continue keyword it execute else part
only time the else part not execute is that met break keyword
normal flow also print else part
else is the way that find break keyword found or not if found it will not execute else part

'''