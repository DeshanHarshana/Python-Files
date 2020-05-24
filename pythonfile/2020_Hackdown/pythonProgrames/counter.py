from collections import Counter
#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
myString='Deshan Harshana Nawarathna'
print(Counter(myList))
print(Counter(myString))
print(Counter(myString).items())
dic=Counter(myString).items()

dict=Counter(myString)
print(dict['a'])
print(dict.keys())
print(dict.values())
