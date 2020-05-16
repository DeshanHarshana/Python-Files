'''
width=20
string="Hackerrank"
print(string.ljust(width,'*'))
print(string.rjust(width,'*'))
print(string.center(width,'*'))
'''
s='H'
len=5
for i in range(1,len+1):
    print(('H'*((2*i-1))).center(len*2),end='\n',sep='')
for i in range(len+1):
    print((s*len).center((2*len),' '),' '*(len*2),(s*len).center((2*len),' '),sep='',end='\n')
for i in range(len-2):
    print((s*((len*len+1)+(((len*2-1)-len)//2))).rjust(len*(len+1),' '),end='\n')
for i in range(len+1):
    print((s*len).center((2*len),' '),' '*(len*2),(s*len).center((2*len),' '),sep='',end='\n')
for i in range(len,0,-1):
    print((('H'*((2*i-1))).center(len*2)).rjust(len*(len+1),' '),end='\n',sep='')
