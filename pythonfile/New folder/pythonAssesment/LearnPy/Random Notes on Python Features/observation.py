ls=list(range(1,11))
a1,*b1,c1,d1=ls
print(a1)#print-1
print(b1)#print-[2, 3, 4, 5, 6, 7, 8]
print(c1)#print -9
print(d1)#print -0
a2, b2, *c2, d2, e2 = ls
print(a2,b2)#print 1,2
print(c2)#print [3, 4, 5, 6, 7, 8]
print(d2,e2)#print 9,10
*x,y=ls #x=[1,2, 3, 4, 5, 6, 7, 8,9]
#p,*q,r,*s,t=ls#error occur can't put two starred expressions in assignment 