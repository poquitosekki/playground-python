# Sets are just a collection of UNORDERED and UNREPEATED elements

# create an empty_set
empty_set = set()
print(empty_set)

set1 = {"Paul", "Max"}
set2 = {"Max", "Euler", "Bob"}
print(set1, set2)

print("UNION METHOD")
print(set1.union(set2))
print("INTERSECTION METHOD")
print(set1.intersection(set2))
print("DIFFERNCE METHOD")
print(set1.difference(set2))
