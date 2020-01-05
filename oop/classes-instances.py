# 1. Python and OOP

# Classes and inheritance


class Employee:
    # this is an initializing method
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.name, self.last)

    def fullname(self):
        return "{} {}".format(self.name, self.last)


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

print(emp1, emp2)
print(emp1.email)
print(emp2.email)

print(emp1.fullname())
# print(emp2.fullname()) # the same as bellow
Employee.fullname(emp1)
