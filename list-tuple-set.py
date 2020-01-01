#########################
# DEFINITIONS
#########################

# Lists :
courses = ['Python', 'Git', 'Github', 'Pandas']
print(courses)
print(len(courses))
print(courses[0], courses[-1])
print(courses[1:3])

# Append (add) to the last index of the list
courses.append("Numpy")
print(courses)
# Append (insert) in a specific index (Takes 2 Arguments)
courses.insert(0, "How to Think ?")
courses.insert(2, "Turtles")
print(courses)

# Add a list
courses2 = ["Tkinter", "TensorFlow"]
# This is going to add a list inside of the other list
# courses.insert(0, courses2)
# And this is not what we want
# we want to add the elements of the courses2 inside of courses
courses.extend(courses2)  # takes only 1 Argument
print(courses)

# Removing an element
courses.remove("How to Think ?")
# Removing the last element of the list and RETURN IT
popped = courses.pop()
print(f"The Popped value is : {popped}")
print(courses)

# Reverse a list
courses.reverse()
print(courses)

# Sort a list (Alphabetilcly)
courses.sort()
print(courses)

nums = [86, 77, 83, 27, 79, 96, 67, 75, 52, 21]
nums.sort()
print(nums)

# Sorting in the REVERSE ORDER
courses.sort(reverse=True)
nums.sort(reverse=True)
print("REVERSE SORTED LISTS")
print(courses)
print(nums)

# If we don't wanna sort the original list
# We can use the sorted(list) method that returns a sorted copy of the LIST
# We wanted to sort
sorted_courses = sorted(courses)
print(sorted_courses)

# Other useful built in functions
print(min(nums))
print(max(nums))
# This sums all of the elements in the num list
print(sum(nums))

# Search in List , AKA : find by index
prog_lang = ["Python", "Java", "Coq", "Lean", "Rust"]
print(prog_lang)
# Get where exactly is the element in the list (Get index)
print(prog_lang.index("Coq"))
# If the element does not exist it simply throws an ERORR on you !
# print(prog_lang.index("PHP"))

# Check if an element in in the list
print("Rust" in prog_lang)  # True
print("R" in prog_lang)  # False

# Looping (iterating) through LISTS
for topic in courses:
    print(topic)

# Access the element and its index
# this is quite useful in some sort of situations
# don't forget to use the enumerate()
# enumerate() returns the index and the value

for index, topic in enumerate(courses, start=1):
    print(index, topic)

# Joining the items of a list in one String => Using join()
# don't forget to add the SEPARATOR before the join method

courses_str = ', '.join(courses)
prog_lang_str = ' - '.join(prog_lang)
print(courses_str)
print(prog_lang_str)

# Spliting the String into a list
new_list = prog_lang_str.split(' - ')
print(new_list)
