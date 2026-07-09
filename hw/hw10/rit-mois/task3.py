class Employee:
    """Employee class with name and salary."""

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def total_employees(cls):
        print("Total number of employees:", cls.counter)

    def employee_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")


emp1 = Employee("Rita", 2000)
emp2 = Employee("Dima", 3000)

Employee.total_employees()
emp1.employee_info()
emp2.employee_info()

print("Base class:", Employee.__base__)
print("Class namespace:")
# key, value in Employee.__dict__.items():
#    print(f'  {key}:{value}')
for key in Employee.__dict__:
    print(f'  {key}')
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
