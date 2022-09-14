class Animal:
    def make_a_sound(self):
        print('Издаёт звук')

class Cat(Animal):
    def __init__(self):
        super().__init__()
    def scratch(self):
        print('Царапать мебель')
    def make_a_sound(self):
        print('Мяу')


class Dog(Animal):
    def __init__(self):
        super().__init__()
    def dig(self):
        print('Рыть землю')
    def make_a_sound(self):
        print('Гав')

Cat=Cat()
Cat.make_a_sound()
Dog=Dog()
Dog.make_a_sound()