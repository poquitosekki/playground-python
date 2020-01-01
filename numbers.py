num = 3
pi = 3.14
# The type function return the variable data type
print(type(num))  # <class 'int'>
print(type(pi))  # <class 'float'>

#########################
# THE REFERENCE
#########################

# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2     # Returns the remainder

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)  # This is Floor division
print(3 ** 2)
print(3 % 2)

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num = 21
num //= 4  # This is the same as { num = num // 4 }
print(num)

num_1 = "100"
num_2 = "200"

print(num_1 + num_2)

# So to return those values to integers do "CASTING"
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)
