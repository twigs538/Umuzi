class Animal:
    def __init__(self, name=None):
        self.name = name
    
    def eat(self):
        return f"{self.name} eats"
    
    def sound(self):
        return "sound..."
        
class Dog(Animal):
    def __init__(self, name='Rax'):
        super().__init__(name)

    def sound(self):
        return "Bark"

class Cat(Animal):
    def __init__(self, name='Stormy'):
        super().__init__(name)

    def sound(self):
        return "Meow"
        
class Home:
    def __init__(self):
        self.adopted_pets = []
        
    def adopt_pet(self, pet):
        if pet in self.adopted_pets:
            raise ValueError('Cannot adopt the same pet twice!')
        self.adopted_pets.append(pet)
        return len(self.adopted_pets)
    
    def make_all_sounds(self):
        sounds = [pet.sound() for pet in self.adopted_pets]
        return sounds or None

if __name__ == '__main__':
    home = Home()

    dog1 = Dog()
    dog2 = Dog('Simba')
    cat1 = Cat()
    cat2 = Cat('Smokey')

    print(home.make_all_sounds())
    print(home.adopt_pet(dog1))
    print(home.adopt_pet(cat1))
    print(home.make_all_sounds())

    print(home.adopt_pet(dog2))
    print(home.adopt_pet(cat2))
    print(home.make_all_sounds())

    dog1 = Dog()
    dog2 = Dog('Simba')

    cat1 = Cat()
    cat2 = Cat('Smokey')

    print(dog1.eat())
    print(dog1.sound())

    print(dog2.eat())
    print(dog2.sound())

    print(cat1.eat())
    print(cat1.sound())

    print(cat2.eat())
    print(cat2.sound())