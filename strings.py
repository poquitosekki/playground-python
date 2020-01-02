# One way to remember how slices work is to think of the indices
# as pointing between #characters, with the left edge
# of the first character numbered 0. Then the right edge
# of the last character of a string of n characters has
# index n, for example:

"""
    REMEMBER HOW SLICING WORK :
     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
     0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1
"""

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
