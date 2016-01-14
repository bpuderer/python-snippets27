#enumerate
print list(enumerate("abcdefg"))
print list(enumerate("abcdefg", start=2))

cardinal_directions = ['north', 'south', 'east', 'west']
for idx, direction in enumerate(cardinal_directions):
    print idx, direction


#hex
print "13 in base 10 is", hex(13), "in hexadecimal"


#format
print "and {} for {} completely {}".format("now", "something", "different")
print "and {when} for {1} completely {0}".format("different", "something", when="now")
print "{:0>+8.2f}".format(3.14159)
print format(42, "08x")


#range and xrange
#http://stackoverflow.com/a/135114
print range(10, 0, -2)

print type(xrange(10, 0, -2))
for i in xrange(10, 0, -2):
    print i


#prompt for input
user_input = ''
while not user_input:
    user_input = raw_input("Enter something so we can move on: ")
print "You entered:", user_input


#zip
list_a = ['a', 'b', 'c']
list_b = [0, 1, 2]
zipped = zip(list_a, list_b)
print list_a, "and", list_b, "zipped:", zipped
print "to dictionary:", dict(zip(list_a, list_b))
print "unzipped:", zip(*zipped)


#map
def double(x):
    return x*2

numbers = [9, 4, 17]
print map(double, numbers)
print map((lambda x: x*2), numbers)


#filter
def ends_in_r(x):
    return x[-1] == 'r'

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
print filter(ends_in_r, months)
