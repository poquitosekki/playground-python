# import modules as mod
# form modules import * (everything)
from modules import find_index, test
import sys


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
