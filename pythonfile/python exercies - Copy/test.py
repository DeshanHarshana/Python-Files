'''
lst=[2,3,4,5]
print('-------------------------')
for i in lst:
    print(i, end='\n')

s='W'
result=False
for i in s:
    if(i.islower()):

        if(not i.isdigit() and  i.isalpha()):
            result=True
        
print(result)
result=False
'''
width=20
string="H"
print(string.ljust(width,'*'))
print(string.rjust(width,'*'))
print(string.center(width,'*'))