class Employee:
    """This class represents an employee and tracks the total number of employees created."""
    
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    @classmethod
    def display_total_employees(cls):
        print(f"Total number of employees: {cls.total_employees}")

    def display_employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

print("\n--- Built-in Class Attributes ---")
print(f"1. Base class (__base__): {Employee.__base__}")
print(f"2. Class namespace (__dict__): {Employee.__dict__}")
print(f"3. Class name (__name__): {Employee.__name__}")
print(f"4. Module name (__module__): {Employee.__module__}")
print(f"5. Documentation (__doc__): {Employee.__doc__}")