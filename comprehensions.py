nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_list = []

# We want n for each n in nums assign it to my_list
# Traditional method
# for n in nums:
#     my_list.append(n)
# print(my_list)

# List comprehension
# We want n for each n in nums
# my_list = [n for n in nums]
# print(my_list)

############################################

# We want n*n for each n in nums
# Traditional method
# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)

# List comprehension
# my_list = [n*n for n in nums]
# print(my_list)

# Map and lambdas method
# my_list = list(map(lambda n: n*n, nums))
# print(my_list)

############################################

# We want n for each n in nums but if n is even
# Traditional method
# my_list = []
# for n in nums:
#     if n % 2 == 0:
#         my_list.append(n)
# print(my_list)

# list comprehension method
# my_list = [n for n in nums if n % 2 == 0]
# print(my_list)

# Filter and lambdas method
# my_list = list(filter(lambda n: n % 2 == 0, nums))
# print(my_list)

############################################

# We want a number pair from 0123 for each letter in abcd

# Traditional method
# my_list = []
# for letter in "abcd":
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# list comprehension method
# my_list = [(letter, num) for letter in "abcd" for num in range(4)]
# print(my_list)


############################################
# Dictionary comprehensions

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# the Zip funciton just assign every match in a tuple and return it as list
# print(list(zip(names, heros)))

# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)

############################################
# Sets comprehensions

nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

# my_set = {n for n in nums}
# print(my_set)

############################################
# Generator Expressions:

nums = list(range(1, 11))

# Generator Object
# def gen_func(nums):
#     for n in nums:
#         yield n*n
#
#
# my_gen = gen_func(nums)
# print(my_gen)

# Geneartor expression
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)
