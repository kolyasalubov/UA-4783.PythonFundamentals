class Employee:
    """Клас співробітника"""
    number_of_employees = 0
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary 
        Employee.number_of_employees += 1

    def show_info(self):
        return f"Name: {self.name}\nSalary: {self.salary}"

    @classmethod
    def show_count(cls):
        return cls.number_of_employees
    

employee1 = Employee("Іван",1200)
employee2 = Employee("Дмитро",2200)
employee3 = Employee("Степан",11200)
employee4 = Employee("Сергій",16200)
employee5 = Employee("Денис",200)
employee6 = Employee("Максим",900)
    
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
print(Employee.__base__)



