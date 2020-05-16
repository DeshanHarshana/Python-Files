import re
def getNumbers(str): 
    array = re.findall(r'[0-9]+', str)
    return list(array)
def getString(str):
    array = ''.join(list([i for i in str if not i.isdigit()])) 
    return list(array)

lst=getNumbers("deshan34,4jsjssn442-923,43232woe;ada3e41")
print(lst)
lst=getString("deshan34,4jsjssn442-923,43232woe;ada3e41")
print(lst)