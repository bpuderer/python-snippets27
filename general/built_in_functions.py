import calendar


#enumerate
print list(enumerate("abcdefg"))
print list(enumerate("abcdefg", start=2))

cardinal_directions = ['north', 'south', 'east', 'west']
for idx, direction in enumerate(cardinal_directions):
    print idx, direction


#iteritems
a_dict = {'north': 0, 'south': 1, 'east': 2, 'west': 3}
for key, val in a_dict.iteritems():
    print key, val

#with keys sorted
for key, val in sorted(a_dict.iteritems()):
    print key, val


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
#xrange renamed to range in python 3
#to gen a list with range in python 3: list(range(n))
print range(10, 0, -2)

print type(xrange(10, 0, -2))
for i in xrange(10, 0, -2):
    print i


#prompt for input
user_input = ''
while not user_input:
    user_input = raw_input("Enter something so we can move on: ")
print "You entered:", user_input


#zip- from PSF- returns list of tuples where the i-th tuple contains
#the i-th element from each of the argument sequences or iterables
#in python 3, zip returns an iterator instead of a list
list_a = ['a', 'b', 'c']
list_b = [0, 1, 2]
zipped = zip(list_a, list_b)
print list_a, "and", list_b, "zipped:", zipped
print "to dictionary:", dict(zip(list_a, list_b))
print "unzipped:", zip(*zipped)

mtrx = [[1, 2, 3], [4, 5, 6]]
print "matrix:", mtrx, "transposed:", zip(*mtrx)


#map- apply function to every item of iterable and return list
def double(x):
    return x*2

numbers = [9, 4, 17]
print map(double, numbers)
print map(lambda x: x*2, numbers)


#filter- return list of items of iterable where function returns true
def ends_in_r(x):
    return x[-1] == 'r'

months = list(calendar.month_name)[1:]
print filter(ends_in_r, months)
print filter(lambda x: x[-1] == 'r', months)


#reduce- reduce items of iterable to single val with function with 2 args
print range(1, 6), "((((1*2)*3)*4)*5) =", reduce(lambda x, y: x*y, range(1, 6))


#all- return true if all items of iterable are true
print all(x[-1] == 'r' for x in months)
#any- return true if any item of iterable is true
print any(x[-1] == 'r' for x in months)


#sorted- return sorted list from iterable
#key is a one arg function that specifies element's comparison key
lod = [{'a': 1}, {'a': 0}, {'a': -1}]
print "list:", lod, "sorted via 'a' key:", sorted(lod, key=lambda x: x['a'])
print "reverse sorted:", sorted(lod, key=lambda x: x['a'], reverse=True)

a_list = ['a', 'ab', 'c', 'abcd', 'abc', 'a']
print "list:", a_list, "sorted by element length:", sorted(a_list, key=len)


#isinstance
class Test1(object):
    pass

class Test2(Test1):
    pass

a = Test1()
b = Test2()

print "Test2 is derived from Test1.  a is instance of Test1, b is instance of Test2"

print "type(a) is Test1:", type(a) is Test1
print "type(b) is Test1:", type(b) is Test1
print "type(a) is Test2:", type(a) is Test2
print "type(b) is Test2:", type(b) is Test2
print "isinstance(a, Test1):", isinstance(a, Test1)
print "isinstance(b, Test1):", isinstance(b, Test1)
print "isinstance(a, Test2):", isinstance(a, Test2)
print "isinstance(b, Test2):", isinstance(b, Test2)


#clear a list
a_list = [1, 2, 3, 4]
print "a_list:", a_list
del a_list[:]
#a_list[:] = [] also cool
print "a_list cleared:", a_list


#clear a dictionary
a_dict = {'a': 1, 'b': 2}
print "a_dict:", a_dict
a_dict.clear()
print "a_dict cleared:", a_dict


#reverse a list in place
#also see slicing.py
a_list = [0, 1, 2, 3]
print a_list, "reversed in place:",
a_list.reverse()
print a_list
