class MyClass:
    # Class attribute (shared among all instances)
    class_attribute = "I am a class attribute"
    
    # Instance initializer (constructor)
    def __init__(self, value):
        self.instance_attribute = value
    
    # Bound method (requires 'self')
    def bound_method(self):
        # Accessing instance attribute
        print(f"Instance Attribute: {self.instance_attribute}")
    
    # Unbound method (doesn't use 'self')
    @staticmethod
    def unbound_method():
        print("I am an unbound method (staticmethod) and do not depend on an instance.")
    
    # Another unbound method using classmethod
    @classmethod
    def class_method(cls):
        print(f"Class Attribute: {cls.class_attribute}")

print("# Create an instance of MyClass")
obj = MyClass("Hello")

print("# Bound method: requires 'self' and has access to instance attributes")
obj.bound_method()  # Output: Instance Attribute: Hello

print("# Unbound method: does not require self, and can be called the instance:")
obj.unbound_method()

print("# Unbound method: does not require 'self', can be called directly from the class")
MyClass.unbound_method()  # Output: I am an unbound method (staticmethod) and do not depend on an instance.

print("# Unbound class method: works at the class level and can access class attributes")
MyClass.class_method()  # Output: Class Attribute: I am a class attribute

print("# Unbound class method: can also be called by the instance:")
obj.class_method()
