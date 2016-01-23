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


#dir
print dir()
print dir({})
print dir(list)
import re
print dir(re)


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


#map- apply function to every item of iterable and return list
def double(x):
    return x*2

numbers = [9, 4, 17]
print map(double, numbers)
print map(lambda x: x*2, numbers)


#filter- return list of items of iterable where function returns true
def ends_in_r(x):
    return x[-1] == 'r'

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
print filter(ends_in_r, months)
print filter(lambda x: x[-1] == 'r', months)


#all- return true if all items of iterable are true
print all(x[-1] == 'r' for x in months)
#any- return true if any item of iterable is true
print any(x[-1] == 'r' for x in months)


#isinstance
class Test1(object):
    pass

class Test2(Test1):
    pass

a=Test1()
b=Test2()

print "Test2 is derived from Test1.  a is instance of Test1, b is instance of Test2"

print "type(a) is Test1:", type(a) is Test1
print "type(b) is Test1:", type(b) is Test1
print "type(a) is Test2:", type(a) is Test2
print "type(b) is Test2:", type(b) is Test2
print "isinstance(a, Test1):", isinstance(a, Test1)
print "isinstance(b, Test1):", isinstance(b, Test1)
print "isinstance(a, Test2):", isinstance(a, Test2)
print "isinstance(b, Test2):", isinstance(b, Test2)
