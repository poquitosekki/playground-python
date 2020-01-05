import datetime
# 3. Python and OOP

# Regular Methods, Class Methods & Static Methods
# RM : takes the instance (self) as the first argument
# CM : takes the class (cls) as the first argument
# SM : don't pass anything automaticlly
# they are like regular funtions but we add them because
# they habe a logical connection to the Class


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.name, self.last)

        Employee.num_of_emps += 1

    # Regular Methods : Get the Self as arg
    def fullname(self):
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Methods : Get a Class as arg
    @classmethod
    # we use the decorator to get the class instead of the instance 'self'
    # as the first argument
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # using the classmethod as ALTERNATIVE CONSTRUCTOR
    # to create instances (name convention = def from_x)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    # We didn't use the self or cls in our method so we use a static one
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

# We're using a @classmethod to iteract with Class variables
Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp_str_3 = "John-Doe-70000"
emp_str_4 = "Ayman-Belhaj-45000"
emp3 = Employee.from_string(emp_str_3)
emp4 = Employee.from_string(emp_str_4)
print(emp3.email)
print(emp4.email)


my_date = datetime.date(2020, 1, 6)
print(Employee.is_workday(my_date))
