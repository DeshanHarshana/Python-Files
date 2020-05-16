s='WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
result=False
for i in s:
    
    if(i.isalnum()):
        result=True
print(result)
result=False

for i in s:
    
    if(i.isalpha()):
        result=True
print(result)
result=False

for i in s:
    
    if(i.isdigit()):
        result=True
print(result)
result=False

for i in s:
    if(i.islower()):
        if(not i.isdigit() and  i.isalpha()):
            result=True
        
print(result)
result=False

for i in s:
    if(i.isupper()):
        if(not i.isdigit() and i.isalpha()):
            result=True
        
        
print(result)
result=False