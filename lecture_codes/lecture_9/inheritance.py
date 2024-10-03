

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

class Cat(Animal):
    def speak(self):
        print("meow")
    
    # overrite super str
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)


cat = Cat(4)
cat.set_name("killer")
cat.speak()
