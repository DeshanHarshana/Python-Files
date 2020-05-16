s=input()
news=[]
for i in s:
    
    x=""
    if(i.isalpha()):
        
        if(i.islower()):
            
            x=i.upper()
        else:
           
            x=i.lower()
    else:
        x=i
    
    news.append(x)
st=""
print(st.join(news))