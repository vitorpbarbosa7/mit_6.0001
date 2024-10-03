from animal import Animal

class Person(Animal):
    def __init__(self, name, age):
        # no need to say self.age = age again
        # but when instantiated the Person, also need to say the age
        Animal.__init__(self, age)
            
        # set name
        self.set_name(name)
        # create new data attribute
        self.friends = []
    
    # easy to ask llm to create getters and setters
    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age = other.age
        print(abs(diff), "year difference")

    def __str__(self):
        return "person"+str(self.name)+":"+str(self.age)

p = Person('Depression', 4)
p.add_friend('Rivotril')
p.speak()
