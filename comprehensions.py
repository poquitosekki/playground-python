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
