marks=[35, 38, 39, 40, 45]
for mark in marks:
    if (mark > 39): grade = 'Pass'
    else: grade = 'Fail'
    print("The result for", mark, 'is', grade)

'''
output
The result for 35 is Fail
The result for 38 is Fail
The result for 39 is Fail
The result for 40 is Pass
The result for 45 is Pass
'''