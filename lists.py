# Guide to Lists

# 1. Create a LIST
# 2. Add and Remove a LIST
# 3. Reverse a LIST
# 4. Sort a LIST
# 5. Search in LIST
# 6. Useful Methods in LIST
# 7. Looping in LIST
# 8. Join and Split

print("ORIGINAL")
prog_lang = ["Python", "R"]
print(prog_lang)

print("APPEND")
prog_lang.append("PHP")
print(prog_lang)

print("INSERT")
prog_lang.insert(1, "Rust")
print(prog_lang)

print("REMOVE")
prog_lang.remove("R")
print(prog_lang)

print("POP")
php_pop_holder = prog_lang.pop()
print(php_pop_holder, prog_lang)

print("EXTEND WITH OTHER LISTS")
add_lang = ["C", "C++"]
print(add_lang)
prog_lang.extend(add_lang)
print(prog_lang)

#################################

print("REVERSE LISTS")
nums = [86, 77, 83, 27]
print(nums)
print(prog_lang)

nums.reverse()
print(nums)
prog_lang.reverse()
print(prog_lang)
# another method to reverse
# does not override the origin list
rev = list(reversed(nums))
print("reversed : {}".format(rev))

#################################
# Sort from A to Z
prog_lang.sort()
print(prog_lang)
# Sort reverse form Z to A
prog_lang.sort(reverse=True)
print(prog_lang)
# another method to sort
# does not override the origin list
sorted_prog_lang = sorted(prog_lang)
print(sorted_prog_lang)

#################################

fruits = ["apple", "orange", "kiwi"]
inx = fruits.index("orange")
print(f"The index of Orange is : {inx}")

isKiwi = "kiwi" in fruits
print(f"is Kiwi in ? : {isKiwi}")

#################################

nums2 = [86, 77, 83, 27]
print("The Max : {}".format(max(nums2)))
print("The Min : {}".format(min(nums2)))
print("The Sum : {}".format(sum(nums2)))

#################################

animes = ["Clannad", "AOT", "SAO"]

for i in animes:
    print(i)

for index, name in enumerate(animes, start=1):
    print(index, name)

str_animes = " - ".join(animes)
print(str_animes)

str_mobiles = "Samsung, Apple, OnePlus"
mobiles = str_mobiles.split(", ")
print(str_mobiles)
print(mobiles)
