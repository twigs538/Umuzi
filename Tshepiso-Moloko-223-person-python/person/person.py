class Person:

    def __init__(self, name, age, gender, interests = None):
        self.name = name
        self.age = age
        self.gender = gender
        if interests is None:
            self.interests = []
        else:
            self.interests = interests

    def interest(self):
        if self.interests:
            if len(self.interests) == 1:
                return f"My interest is {self.interests[0]}"
                
            return f"My interests are {', '.join(self.interests[:-1])} and {self.interests[-1]}"    

        else:
            return "I have no interests"

    def hello(self):
        return f"Hello, my name is {self.name}, my gender is {self.gender} and I am {self.age} years old. {self.interest()}."

if __name__ == '__main__':
    person = Person('Ryan', 30, 'male', ['o','k','l'])
    greeting = person.hello()
    print(greeting)