
lst=list(map(int,input().split()))
width=lst[1]
height=lst[0]
if(height*3==width):
    s='.|.'
    for i in range(1,(height//2)+1):
        print((s*(2*i-1)).center(width,'-'))
    print('WELCOME'.center(width,'-'))
    for i in range((height//2),0,-1):
        print((s*(2*i-1)).center(width,'-'))
