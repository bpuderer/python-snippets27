import os.path


test_file = 'temp.txt'

# use with() to ensure file is closed
# 'w' overwrites, 'a' appends, 'r' for reading, 'r+' for reading and writing
# add 'b' to end for binary files in Windows, 'wb', 'ab', 'rb', 'r+b'
# can also use multiple open statements within single with()
# ex. with open('temp1.txt') as f1, open('temp2.txt') as f2:
with open(test_file, 'w') as f:
    print "wrote", test_file
    f.write('first line\n')
    f.write('second line\n')
    f.write('third line?\n')

print "Does", test_file, "exist?", os.path.isfile(test_file)

with open(test_file, 'a') as f:
    lines = ['fourth line\n', 'fifth line\n']
    f.writelines(lines)

with open(test_file, 'a') as f:
    lines = ['sixth line', 'seventh line']
    f.write('\n'.join(lines) + '\n')

with open(test_file, 'a') as f:
    lines = ['eighth line', 'ninth line']
    for line in lines:
        f.write('{}\n'.format(line))

print "-----"

# line by line
# mode 'r' (read) is the default
print "line by line over", test_file
with open(test_file, 'r') as f:
    for line in f:
        print line,

print "-----"

# read single line
print "first line from", test_file
with open(test_file) as f:
    print f.readline(),

print "-----"

# read all lines into list
print "all lines in", test_file, "as a list"
with open(test_file) as f:
    print f.readlines()

print "-----"

# read entire file at once
print "all lines in", test_file, "as a string"
with open(test_file) as f:
    print f.read()
