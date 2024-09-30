class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(f"Employee {self.name} initialized with salary {self.salary}")

    def get_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, team):
        # no need to write the initialization of name and salaray again
        super().__init__(name, salary)  # Initialize Employee attributes
        self.team = team  # Manager-specific attribute
        print(f"Manager {self.name} is managing a team of {len(self.team)}")

    def get_info(self):
        base_info = super().get_info()  # Get basic employee info
        return f"{base_info}, Manages: {', '.join(self.team)}"

# Example usage:
manager = Manager("Alice", 120000, ["John", "Doe", "Emma"])
print(manager.get_info())

