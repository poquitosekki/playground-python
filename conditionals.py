# CONDITION

lang = "Python"

if lang == "Python":
    print("Language is Python")
elif lang == "Perl":
    print("Language is Perl")
else:
    print("Language is NOT Python")

# Note : Python does not have a Switch case statement

user = "Admin"
logged_in = True

if user == "Admin" and logged_in:
    print("The Admin is logged in !")

if not logged_in:
    print("Please log in")
else:
    print("Welcome !")

a = [1, 2, 3]
b = [1, 2, 3]

# They have the same value so it's True
print(a == b)
# But they are totally different objects in Memory
print(a is b)
# to print the location id (They are different !)
print(id(a))
print(id(b))

# False values
# False
# None
# Zero of any NUMERIC type
# Any empty sequence. for example "", (), []
# Any empty maping (empty dict). for example {}

condition = set()

if condition:
    print("TRUE")
else:
    print("FALSE")
