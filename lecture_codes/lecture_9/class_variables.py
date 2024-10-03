

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None 

    # getters
    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
    
    # setters
    def set_age(self, newage):
        self.age = newage

    def set_name(self, newname):
        self.name = newname
        
    def __str__(self):
        return "animal:"+ str(self.name) + ":"+str(self.age)


class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1
        
    def __add__(self, other):
        return Rabbit(
                age = 0, 
                parent1 = self, 
                parent2 = other)


r1 = Rabbit(2)
r2 = Rabbit(6)

print(r1.rid)
print(r2.rid)

# uses the __add__
new_r = r1 + r2
print(new_r.age)
