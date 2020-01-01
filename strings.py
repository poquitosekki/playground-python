message = "Hello CTF"
print(message)

long_message = """
    This is a multiline
    String and will be printed
    with the same formating
    that i'am writing it by.
"""
print(long_message)

# Printing the length of a String
print(len(long_message))  # 113
print(message[6])  # C
print(message[6:])  # print from 6 to the end "CTF"

# String Methods

str = "Hello Python 3"
print(str.lower())
print(str.upper())
print(str.count("l"))  # 2 times
print(str.find("Python 3"))
print(str.replace("Python 3", "Java"))

greeting = "Hey"
name = "Max"

# Methods of Formating
greet = greeting + ", " + name
greet = "{}, {}".format(greeting, name)
greet = f"{greeting}, {name.upper()}"
print(greet)

# Show the available string methods
print(dir(greet))
