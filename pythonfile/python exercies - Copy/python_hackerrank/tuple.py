n=int(input())


tpl=tuple(map(int,input().split()))
if len(tpl)==n:
    print(hash(tpl))
