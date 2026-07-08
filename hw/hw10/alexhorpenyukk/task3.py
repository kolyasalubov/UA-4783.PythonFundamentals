class Employee:
    '''The class for employee storing'''

    employees_counter = 0

    def __init__(self, name, salary):
        Employee.employees_counter += 1
        self.name = name
        self.salary = salary

    @classmethod
    def total_employees(cls):
        print(f'There are {cls.employees_counter} employees in the company')

    def employee_info(self):
        print(f'Employee {self.name} gets {self.salary}$')

e1 = Employee('Anton', 3000)

print(Employee.__base__)
print()
print(Employee.__dict__)
print()
print(Employee.__name__)
print()
print(Employee.__module__)
print()
print(Employee.__doc__)