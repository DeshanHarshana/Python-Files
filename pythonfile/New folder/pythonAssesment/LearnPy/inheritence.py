class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

#Create a Child Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
#if child class init and parent class init has same parameter even if we add parent class student init to data
#child class override it and execute child class printname

x = Student("Mike", "Olsen")
x.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname) #we can't use Person.__init__(fname,lname) because parent and child parameters are not same
        self.graduationyear = year
    def printname(self):
        return super().printname()
x = Student("Misadske", "Osdadlsen", 2019)
print(x.graduationyear)
x.printname()
print(x.firstname)
x.printname()

