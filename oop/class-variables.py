# 2. Python and OOP

# Class Variables
# are variables that are shared with all instances of a class
# You can access it from both the class attr and the instances attr
# but they just get it from the class it self or the class of the class HAHA
# IF you change this value in the CLASS it changes in every instance
# BUT if you change it in an INSTANCE the value changes in that name space
# this is a good thing to include
# But with something like "NUMBERS OF EMPLOYEES" we have no use case
# to override that value using an instance


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.name, self.last)

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        # using self give the sub_classes and instances the ability to
        # override the class value
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

print(emp1.__dict__)
print(Employee.__dict__)

# emp1.raise_amount
# Employee.raise_amount

print(emp1.pay)
emp1.apply_raise()
print(emp2.pay)

print(Employee.num_of_emps)
