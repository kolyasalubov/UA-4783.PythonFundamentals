class Employee(object):
    """This class store info about employees"""
    
    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.name = name
        self.salary = salary

    def __del__(self):
        Employee.counter -= 1

    def count_employee():
        print(Employee.counter)

    def info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

emp1 = Employee("Ivan", 1000)

print(Employee.__base__)
print(emp1.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
