class Employee: 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def increase_salary(self, percentage):
        self.salary = self.salary* (1+ percentage / 100) #asked chat another way to put in prectage cause I did % and it didn't work :(

john = Employee("John", 5000)

john.increase_salary(10)

print("Jhon's new salary is:", john.salary)