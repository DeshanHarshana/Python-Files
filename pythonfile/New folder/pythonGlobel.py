x=0
class Test:
    name=""
    age=0
    
        

    def setter(self, name, age):
        self.age=age*9
        global x 
        x=34
        
        print(x)
        
    

obj1=Test()
obj1.setter('Deshan', 21)
print(obj1.age)
print(x)



