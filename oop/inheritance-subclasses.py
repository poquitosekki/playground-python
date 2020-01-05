# 4. Inheritance - Creating Subclasses
#
#
#


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
        self.pay = int(self.pay * self.raise_amount)

# Sub Class


class Developer(Employee):

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # let the super Class handle the repeated data
        super().__init__(first, last, pay)
        # Other method
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("===>", emp.fullname())


# Outputs
dev1 = Developer("Corey", "Schafer", 50000, "Python")
dev2 = Developer("Test", "Employee", 60000, "Java")

# Return information about our class
# print(help(Developer))

# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
#
# print(dev1.email)
# print(dev1.prog_lang)

mgr1 = Manager("Sue", "Smith", 90000, [dev1])
# print(mgr1.email)
# mgr1.add_emp(dev2)
# mgr1.remove_emp(dev1)
# print(mgr1.print_emps())


# Helpful methods (isinstance, issubclass)
print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employee))
print(isinstance(mgr1, Developer))  # False

print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))  # False
