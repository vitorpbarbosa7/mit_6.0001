class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Salary is now private (denoted by __).

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary with validation
    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative!")
        self.__salary = salary

# Create an employee
employee = Employee("Alice", 50000)

# Use the setter to safely update salary
try:
    employee.set_salary(-10000)  # This will raise an exception.
except ValueError as e:
    print(e)  # Output: Salary cannot be negative!

# Use the getter to access the salary safely
print(employee.get_salary())  # Output: 50000

