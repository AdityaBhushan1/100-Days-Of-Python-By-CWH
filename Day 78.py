class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name, species = "Cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!")

d = Dog("Dog","Doggerman")
c = Cat("Cat","Cheetah")
a = Animal("Dog","Dog")

d.make_sound()
a.make_sound()
c.make_sound()