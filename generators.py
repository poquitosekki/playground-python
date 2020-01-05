# def square_numbers(nums):
#     result = []
#     for i in nums:
#         result.append(i*i)
#     return result


# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)
#
#
# my_nums = square_numbers(list(range(1, 6)))

my_nums = (x*x for x in list(range(1, 6)))
# Generator created using a list comprehension
print(my_nums)
# You loose performence
# because generators does not store all the data at once
# instead it stores one element each time
print(list(my_nums))
for num in my_nums:
    print(num)
