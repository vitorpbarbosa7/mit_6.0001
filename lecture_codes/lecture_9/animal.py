

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


# different names from inside and outside the class
# that is why use getters and setters
class Anima(object):
    def __init__(self, age):
        self.years = age

    def get_age(self):
        return self.years
    

a = Animal(3)

a.age = 'bla'
a.new_data_attribute = 'new'

print(a.get_age())
print(a.age)
print(a.new_data_attribute)
