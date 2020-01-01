# Printing a Welcome message

message = "Hello World"
# Python prints that string with the exact same formating
longMessage = """
    What the hell is this
    this is insane bro's
"""

print(message)
print(longMessage)
print(len(message))
# This returns the last index
print(message[-1])
# Get just hello from the message string
print(message[0:5])

# String methods

# the lower case method
print(message.lower())
# the upper case method
print(message.upper())

# The count method
# It basically returns how many times the "Argument" appears in a String
print(message.count("Hello"))
print(message.count("l"))  # how many times appears l in the message string
# The find method
# It basically returns the index where it finds the "Argument" in String
print(message.find("World"))
print(message.find("d"))

# The replace method
str = "Hallo World"
str = str.replace("World", "Welt")  # Replace and reassign the value in str var
print(str)

greeting = "Hello"
name = "Paul"

# 3 Methods of Concatenation
greet = greeting + ", " + name + ". Welcome!"
greet = "{}, {}. Welcome!".format(greeting, name)
greet = f'{greeting.upper()}, {name}. Welcome!'
print(greet)

# This prints every method that's available for your String
print(dir(name))
