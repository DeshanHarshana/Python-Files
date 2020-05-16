x='    deshan    harshana    '
z='  deshan  harshana  '
print(x)
y='www.learnpython.com.com'
print(x.lstrip())
print(x.rstrip())
print(x.strip()) #remove whitespaces
x=x.strip('harshana')
print(x)
print(y.strip('w')) # remove w from both side 
print(y.strip('com')) # remove com from both side not.com 
print(y.strip('.com')) # remove .com form bothside 
print(z.strip().strip('harshana'))
print(z.replace(" ", ""))