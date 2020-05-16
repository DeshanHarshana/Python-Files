ls = [12, 7, 5, 22, 25, 34, 20, 83, 45, 82]
lst=[(i, i**2, i**3) for i in ls if i%3==0]
print(lst)
print(type(lst))

product1=[(i) for i in range(1,4)]
product2=[(i,j) for i in range(1,4) for j in range(2,10,2)]
product3=[(i,j,k) for i in range(1,4) for j in range(2,10,2) for k in range(3,10,3)]
print(product1)
print('--------------------------------------------------------------------------------------------')
print(product2)
print('--------------------------------------------------------------------------------------------')
print(product3)
print('--------------------------------------------------------------------------------------------')