
nums = list(range(1, 6))
print(nums)

for num in nums:
    if num == 3:
        print("Found!")
        continue  # Go to the next iteration
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(1, 10):
    print(i)

# The WHILE LOOP
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1
