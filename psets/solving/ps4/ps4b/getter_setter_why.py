class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # Salary should have constraints, but we are not enforcing it here.

# Create an employee
employee = Employee("Alice", 50000)

# Direct access to salary attribute, no validation
employee.salary = -10000  # Negative salary doesn't make sense, but there's no validation.

print(employee.salary)  # Output: -10000, which is incorrect and causes a logic flaw

