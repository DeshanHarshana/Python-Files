class A:
    x=45
    name=''
    age=0
    def __init__(self, name, age):
       self.name=name
    
    def show(self, message, x):
        print(message)
        print(self.x)
    @staticmethod #no need self argument
    def power(i):
        return i*i

com1=A('Deshan', 33)
com1.show('Hello', 2)
print(com1.name)
print(com1.power(2))

#self and this are same