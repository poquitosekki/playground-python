# 5. Special (Magic/Dunder) Methods
# Special methods helps with :
# 1) emulate (Or change) some built-in behaviour within python
# 2) how we implement operator overloading

# if we print an instance, python prints the str and not the __repr__
# but we can access them through repr(inst) & str(inst)


class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    # this may be called a Dunder init
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@company.com".format(self.first, self.last)

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Meant to be seen by other developers (eg. for debugging)
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # Meant to be displayed for the end-user
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

# Dunder length method
# print(len(emp1))
# Dunder add method
# print("The 2 Salarys: ", emp1 + emp2, "\n")

# print(emp1)
# print Employee('Corey', 'Schafer', '50000')
# instead of <__main__.Employee object at 0x1103f5130>
# using the Dunder repr function

print(repr(emp1))
print(str(emp1))

print(1 + 3)
print(int.__add__(1, 3))

##########################
# DUNDER METHODS
##########################

# __abs__
# __add__
# __and__
# __call__
# __class__
# __cmp__
# __coerce__
# __complex__
# __contains__
# __del__
# __delattr__
# __delete__
# __delitem__
# __delslice__
# __dict__
# __div__
# __divmod__
# __eq__
# __float__
# __floordiv__
# __ge__
# __get__
# __getattr__
# __getattribute__
# __getitem__
# __getslice__
# __gt__
# __hash__
# __hex__
# __iadd__
# __iand__
# __idiv__
# __ifloordiv__
# __ilshift__
# __imod__
# __imul__
# __index__
# __init__
# __instancecheck__
# __int__
# __invert__
# __ior__
# __ipow__
# __irshift__
# __isub__
# __iter__
# __itruediv__
# __ixor__
# __le__
# __len__
# __long__
# __lshift__
# __lt__
# __metaclass__
# __mod__
# __mro__
# __mul__
# __ne__
# __neg__
# __new__
# __nonzero__
# __oct__
# __or__
# __pos__
# __pow__
# __radd__
# __rand__
# __rcmp__
# __rdiv__
# __rdivmod__
# __repr__
# __reversed__
# __rfloordiv__
# __rlshift__
# __rmod__
# __rmul__
# __ror__
# __rpow__
# __rrshift__
# __rshift__
# __rsub__
# __rtruediv__
# __rxor__
# __set__
# __setattr__
# __setitem__
# __setslice__
# __slots__
# __str__
# __sub__
# __subclasscheck__
# __truediv__
# __unicode__
# __weakref__
# __xor__
