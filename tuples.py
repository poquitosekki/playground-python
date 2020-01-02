# Tuples are used to loop through and access Data
# You can't change values at certain indexes like a LIST

tuple1 = ("Python", "Turtles")
print(tuple1)

for t in tuple1:
    print(t)

print("LIST OF THECHNOLOGIES I WANNA LEARN :")
for i, t in enumerate(tuple1, start=1):
    print(f"{i}: {t}")
