s='12abc'
def solve(s): 
    a = s.split(' ')

    new_string = ''
    for i in range(0, len(a)) :
        new_string = a[i].capitalize() if len(new_string)==0 else new_string +' '+ a[i].capitalize()
    return new_string
solve(s)