# File Objects

# f = open('/Users/poquito/Desktop/corey/file-objects/what.txt', 'r')
# Flags
# r = read, w = write, a = append, r+ = read and write
# print(f.name)
# print(f.mode)

# don't forget to close the file after what you wanna do with it
# but the with command automaticly close the file for us (so it's recommended)
# f.close()


with open('/Users/poquito/Desktop/corey/file-objects/what.txt', 'r') as f:
    # Work with the file within this block
    # outside this block the file is considered closed

    # you can also specify the how many carac you wanna print
    # f_contents = f.read(250)
    f_contents = f.read()
    print(f_contents)

    # return the lines as a list

    # f_contents_list = f.readlines()
    # print(f_contents_list)

    # print every

    # for line in f:
    #     print(line, end="")

# The write option overrides the text that's already in the file
with open('/Users/poquito/Desktop/corey/file-objects/write.txt', 'w') as w:
    w.write("TEST")
    w.seek(0)
    w.write("R")

# The append option add to the text that's already in the file
with open('/Users/poquito/Desktop/corey/file-objects/append.txt', 'a') as a:
    a.write("TEST APPEND")

path = "/Users/poquito/Desktop/corey/file-objects"
# Get line from the read file (rf) in write them in write file (wf)
with open('/Users/poquito/Desktop/corey/file-objects/what.txt', 'r') as rf:
    with open(f'{path}/write.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
