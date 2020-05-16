def A(marks):
    grade=""
    if 75 <= marks <= 100 :
        grade = 'A+'  
    elif 70 <= marks < 75 :
        grade = 'A'
    elif 60 <= marks < 70 :  
        grade = 'B'
    elif 50 <= marks < 60 : 
        grade = 'C'
    elif 40 <= marks < 50 : 
        grade = 'D+'
    elif 35 <= marks < 40 : 
        grade = 'D'
    elif 25 <= marks < 35 : 
        grade = 'D-'
    else: 
        grade = 'E'
    return grade

def B(marks):
    grade=""
    if  marks  >=75 :
        grade = 'A+'  
    elif  marks  >= 70 :
        grade = 'A'
    elif  marks >= 60:  
        grade = 'B'
    elif 50 <= marks :  
        grade = 'C'
    elif 40 <= marks:  
        grade = 'D+'
    elif 35 <= marks :  
        grade = 'D'
    elif 25 <= marks :  
        grade = 'D-'
    else:  
        grade = 'E'
    return grade

markList=[100,99,71,63,55,44,37,30,5]
print('Marks \t Method A \t Method B')
for i in markList:
    print(i,"\t",A(i),"\t\t",B(i))

# in method A, computer have to check two values before put grade to relevent mark
# but in method B computer have to consider only one value.
# personally i think B method is better than A 