class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = None  # Initialize with None
        self.set_age(age)  # Use setter to validate the initial age

    # Getter for 'age'
    def get_age(self):
        return self._age

    # Setter for 'age' with validation
    def set_age(self, age):
        if age >= 0:  # Ensure age is non-negative
            self._age = age
        else:
            print("Error: Age cannot be negative!")

# Create an instance
p = Person('Alice', 25)

# Access attribute using getter
print(p.get_age())  # Output: 25

# Modify attribute using setter
p.set_age(30)
print(p.get_age())  # Output: 30

# Try to set an invalid age
p.set_age(-5)  # Output: Error: Age cannot be negative!

