class Monkey:
    def __init__(self):
        pass
    def climb(self):
        print('Monkey climb')
    def eat(self):
        print('Monkey eat')

class Human(Monkey):
    def __init__(self):
       pass
    def climb(self):
        print('Human climb')
    def eat(self):
        super().eat()
        print('Human eat')
    def think(self):
        print('Human think')

obj=Monkey()
obj.eat()
obj2=Human()
obj2.eat()