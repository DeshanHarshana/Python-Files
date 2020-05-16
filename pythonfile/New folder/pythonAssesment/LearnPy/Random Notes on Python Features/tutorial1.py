#The in operator is to check the membership of an element in a collections/sequence such as lists, 
# tuples, sets,  and strings.

print('h' in 'python')
fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
  print("yes")

x = ["apple", "banana", "cherry"]

y = x

print(x is y)#memory address are same
print(id(x))
print(id(y))

#The is keyword is used to test if two variables refer to the same object
#The test returns True if the two objects are the same object.
class Com:
    x=10
    y=10
obj1=Com()
print(obj1.x is obj1.y)
print(id(obj1.x))
print(id(obj1.y))


x = ["apple", "banana", "cherry"]

y = ["apple", "banana", "cherry"]

print(x is y)
print(id(x))
print(id(y))
#even if variables apperence are same if memory address is different it return false

ls1 = [1, 2, 3]
ls2 = [1, 2, 3]
ls3 = ls1
print(ls1==ls2)
print(ls1 is ls2)#because it is diffrent memory addrss
print(ls3 is ls1)#true