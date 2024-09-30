class Employee: 
    
    # constructor
    def __init__(self, first, last, pay):
        # instance variables
        # avaiable for all instance methods
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    # simple bounded method, which the class will apply the method to the arguments
    # associated with the instance of the class
    # so binds the instance to that method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # not bounded method
    @staticmethod
    def hi():
        print('hi')

emp_1 = Employee(first='a', last='aa', pay=10)
emp_2 = Employee(first='b', last='bb', pay=20)

# when we call the bounded method, what it really does it is this:
# the transformation 
print("object bounded method being called the the class")
print(Employee.fullname(emp_1))

print("the instances itself")
print(emp_1)
print(emp_2)

print("printing each argument")
print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)
print(emp_1.email)

emp_1.fullname()

print("static method")
print("no need to pass the self as parameter (the instance of the object), because is a unbonded method")
emp_1.hi()
