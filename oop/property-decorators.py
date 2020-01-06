# 6. Property Decorators - Getters, Setters, and Deleters


class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp1 = Employee("John", "Smith")

emp1.first = "Jim"
# Setter
emp1.fullname = "Corey Schafer"
del emp1.fullname

print(emp1.first)
# to access the email function as a property we need a Decorator
print(emp1.email)
print(emp1.fullname)
