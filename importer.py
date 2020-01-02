# import modules as mod
# form modules import * (everything)
from modules import find_index, test
import sys
# The standard Library
import random
import math
import datetime
import calendar
import os

courses = ["Python", "Turtles", "Pandas", "Tkinter", "Numpy"]

# index = modules.find_index(courses, "Pandas")
# index = mod.find_index(courses, "Pandas")
index = find_index(courses, "Pandas")
print(index)
print(test)

# Return the directories where python looks for modules in your System
print(sys.path)

# Add a directory
# METHOD 1
# sys.path.append("add path here")
# METHOD 2
# Set in python path : type in terminal
# nano ~/.bash_profile
# add : export PYTHONPATH="the path here"

# The random module
random_course = random.choice(courses)
print(random_course)

# The math module
rads = math.radians(90)
print(math.sin(rads))

# The datetime, calendar module
today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

# The OS module
# get the current working directory
print(os.getcwd())
# print where os.py lives in your computer
print(os.__file__)
