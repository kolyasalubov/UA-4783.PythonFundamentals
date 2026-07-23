class Employee:
    """
    This class save information about employees,
    namely names and salary,
    count all employees
    and information about this class
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def info(self):
        return f"Name: {self.name}. Salary: {self.salary}"

    @classmethod
    def counter(cls):
        return cls.employee_count

emp1 = Employee("Matviy", 30000)
emp2 = Employee("Diana", 35000)
emp3 = Employee("Volodya", 32000)
emp4 = Employee("Ram", 30000)
print(f"Total number of employees: {Employee.counter()}")

employees = [emp1, emp2, emp3, emp4]

for employee in employees:
    print(employee.info())

print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
print(Employee.__bases__) 