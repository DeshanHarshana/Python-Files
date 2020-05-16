st, m, n = 'Flamboyant', 4, 7
for c in st[m:n] :
    print(c)

for c in st[n:m:-1] :
    print(c)

for e in [13, 4, 5, 89, 4]:
    print(e, e%7)

points = [ (2, 1), (4, 1), (4, 2), (2, 2)]
print(type(points[0]))
print(type(points))
for i in points:
    print(*i, sep='\n')
#if we use sep we have to use * if we use * breaket gone
#sep seperate between all element
#end speprate between sub element
for i in points:
    print(i, end='\n')
for i in points:
    print(i, end=' ')

for i in points:
    print(*i, end=' ')
print('\n-----------------------------------------------------')

for x, y in points:
    print(x)
    print(y)
    print('----')

print('\n-----------------------------------------------------')

pp=list(enumerate([12,45,67],3))# start lebel in 3
print(pp)

cc=list(enumerate('Deshan',3))# start lebel in 3
print(cc)
print('\n-----------------------------------------------------')


ls = [1, 8, 29, 22, 5, 83]
lst=list(enumerate(ls))
print(lst)
dic=dict((enumerate(ls)))
for index, item in enumerate(ls):
    print(index, item)
print(dic.keys())
print(dic.get(0,None))
print(dic.values())
print(dic[5])
print(dic.items())
def get_key(val): 
    for key, value in dic.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"
print(get_key(83))
print('\n-----------------------------------------------------')
ls = [12, 7, 5, 22, 25, 34, 20, 83, 45, 82]
fives=[i for i in ls if i % 5 == 0]
#ls1 = [ i, for i in range(5)]>>>>ls1 = [ i for i in range(5)]
#ls2 = [ i for i in ls : if ls%3] >>> ls2 = [ i for i in ls  if i % 3]
#ls3 = [ (i, i**2) for i in range(10)]
#ls4 = [ (i, i**2) for i in range(5)]
print(fives)

print('\n-----------------------------------------------------')
gen1 = [[i**2] for i in range(1, 5)]#get one and power it and put gen1 get 2 power it and put gen1
gen2 = ([i**2] for i in range(1, 5))# if we use normal paranthesis it generate not list but generator
print(type(gen1))
print(type(gen2))
