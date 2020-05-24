i=int(input())
st=''
for x in range(1,i+1):
    if(x%2==0):
        st=st+str(x)+'#'
    else:
        st=st+str(x)+'*'
print(st)

