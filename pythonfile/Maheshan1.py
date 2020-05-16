lst = [35, 38, 39, 40, 45]
grade = ''
for i in lst:
    if i > 39:
        grade = 'pass'
    else:
        grade = 'fail'
    print("The result for", i, 'is', grade)

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)

numlist = [13, -6, 58, 22, -5, 99, 5, -7, 93, 1, -8, 50]
negno = [x for x in numlist if x < 0]
print(negno)

number=[13, 6, 58, 5, 7, 96, 1, 8, 39]
evennumber=[x for x in number if x%2==0]
print(evennumber)
