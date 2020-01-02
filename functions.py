# FUNCTIONS


def test():
    pass


def say_hello():
    print("Hello from Function!")


for i in range(4):
    say_hello()


def return_hello():
    return "Hello World"


# if you know the type of the return value of a Function
# You can treat it as that type and apply built in function
print(return_hello().upper())


# Parameters, Arguments
def greeting_func(greeting, name="You"):
    return f"{greeting}, {name}."


print(greeting_func("Hi"))  # the name takes the default value "YOU"
print(greeting_func("Hey", "Corey"))


# Open number of ARGS
def student_info(*args, **kwargs):
    print(args)  # Return a tuple
    print(kwargs)  # Return a dictionary with key pair values


courses = ["Math", "Art"]
info = {"name": "John", "age": 34}

student_info("Math", "Art", name="John", age=34)
# The stars give the info of UNPACKING TYPE
student_info(*courses, **info)

month_days = [23, 29, 30, 21, 4, 0, 10, 26, 8]


def is_leap(year):
    # This is doc String = used to help document a class or a Fucntion
    # to know what it's doing
    """Return True for leap Years, and False for non-leap Years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    # a doc String
    """Return number of days in that month in the year."""
    if not 1 <= month <= 12:
        return "Invalid Month"

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(2020))
print(days_in_month(2020, 1))
