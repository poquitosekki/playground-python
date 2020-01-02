# Think of it like a real world dict (key: value)
student = {
    "name": "Paul",
    "age": 23,
    "courses": ["Math", "Computer Science"]
}

print(student)
# Print actual value using key
# if you tried this with a non-existing key it will throw an erorr
courses = " and ".join(student["courses"])
statement = f"The Courses that {student['name']} takes are : {courses}"

# instead we can use the get() method
print(student.get('name'))
print(student.get('email'))  # Returns None (by default)
# Return the error that's passed as a 2nd argument
print(student.get('phone', 'NOT found'))

print(statement)

# updating valus
student["phone"] = '555-5555'
student["name"] = "Jane"

# you can use the update method (dict as argument) (can update multiple vals)
student.update({"name": "ALEX", "age": 19, "phone": "545-5555"})
print(student)

# You can delete a key with the value
del student["age"]
print(student)

courses = student.pop('courses')
print(courses)
print(student)

# Useful Methods (len, keys, values, items)
print(len(student))  # 2 keys
print(student.keys())
print(student.values())
print(student.items())


# looping
# this only access the keys in a dict
for key in student:
    print(key)

# to get the key and the value
for key, value in student.items():
    print(key, "\t", value)  # this \t prints a tab in front of the key
