import os

# Change the working directory
os.chdir("/Users/poquito/Desktop/corey/parse-and-rename-files/files-dir/")

# loop through every file in the List directory
for f in os.listdir():
    if f == '.DS_Store':
        continue
    # From the os.path split the f into "name" and "extension"
    f_name, f_ext = os.path.splitext(f)
    # split the f_name into title, course, number
    f_title, f_course, f_num = f_name.split('-')
    # We want to remove any white space in our title, course or number
    f_title = f_title.strip()
    f_course = f_course.strip()
    f_num = f_num.strip()
    # Create a new name (with number, title and extension)

    # remove the # from every number and make two digit numbering
    # this is quite handy when we have a lot of files
    f_num = f_num[1:].zfill(2)
    new_name = "{}-{}{}".format(f_num, f_title, f_ext)
    print(new_name)

    # Rename the files
    os.rename(f, new_name)
