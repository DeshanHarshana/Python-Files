'''
student_marks = {}
name, *line=input().split()
print(line)
score=list(map(float,line))#get value from line and do float and pass score as list
print(score)
student_marks[name]=score
print(student_marks)
'''

'''
n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
 

 def myfunc(n):
      return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) get apple and put to myFunc do it all set
'''