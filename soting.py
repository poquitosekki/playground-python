from operator import attrgetter

print("Soring lesson")

# li = [3, 6, 7, 7, 87, 2, 0]
# # Does not change the original variable list
# s_li = sorted(li)
# print(f"Non Sorted\t{li}")
# print(f"Sorted\t\t{s_li}")
# # if you wanna change the same variable list (sorted)
# # Sort the list and return None
# # to Sort by reverse use this : 'it works on both of them'
# li.sort(reverse=True)
# print(li)

# print("TUPLES")
# li_tuple = (3, 6, 7, 7, 87, 2, 0)
# print(li_tuple)
# # tuples does not have a .sort() like list
# # instead we can use the sorted method
# # returns the sorted tuple as a LIST !!!!
# tup_srt = sorted(li_tuple)
# print(tup_srt)

# neg_list = [-2, -3, -2, -6, -5, -4, 0]
# srt_list = sorted(neg_list)
# # Using the key param we can sort using a function
# # here we used the built in funcion abs
# # which performs for every element in the list
# srt_by_abs = sorted(neg_list, key=abs)
# print(neg_list)
# print(srt_list)
# print(srt_by_abs)

# Extended Key usage

# Class of employee with a representation function


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return "({}, {} ,${})".format(self.name, self.age, self.salary)


# Create 3 Objects out of this class
e1 = Employee("Carl", 34, 30000)
e2 = Employee("Bob", 36, 60000)
e3 = Employee("Paul", 54, 900000)

employees = [e1, e2, e3]
# We can't sort directly because
# we need to specify how this data will be sorted
# so we need to write a custom function that sort based on something
# This function returns the value that we're gonna sort based on


# def e_sort(employee):
#     return employee.age

# instead of that we can also write a lambda expression
# or we have a attrgetter("attr") inside of operator module that get attr

# sort_employees = sorted(employees, key=e_sort)
# sort_employees = sorted(employees, key=lambda e: e.age)
sort_employees = sorted(employees, key=attrgetter("age"))
print(sort_employees)


class Animal():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return "(Name : {}, Weight : {}Kg)".format(self.name, self.weight)


dog = Animal("Dog", 23)
cat = Animal("Cat", 12)

animals = [dog, cat]


def sort_weight(animal):
    return animal.weight


animals_s = sorted(animals, key=sort_weight)
print(animals)
print(animals_s)
