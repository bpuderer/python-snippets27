import calendar
import itertools
import random
import string


months = list(calendar.month_name)[1:]


#enumerate
print list(enumerate("abcdefg"))
print list(enumerate("abcdefg", start=2))

cardinal_directions = ['north', 'south', 'east', 'west']
for idx, direction in enumerate(cardinal_directions):
    print idx, direction


#bin, hex, oct, format
n = 42
print n, 'in binary is', bin(n), 'and', format(n, 'b'), 'sans prefix'
print n, 'in hex is', hex(n), 'and', format(n, 'x'), 'sans prefix'
print n, 'in octal is', oct(n), 'and', format(n, 'o'), 'sans prefix'


#dir
print dir()
print dir({})
print dir(list)
print dir(calendar)


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
#the i-th element from each of the argument sequences or iterables.
#The returned list is truncated in length to the length of the shortest argument sequence.
#in python 3, zip returns an iterator instead of a list
list_a = ['a', 'b', 'c']
list_b = [0, 1, 2]
zipped = zip(list_a, list_b)
print list_a, "and", list_b, "zipped:", zipped
print "to dictionary:", dict(zip(list_a, list_b))
print "unzipped:", zip(*zipped)

mtrx = [[1, 2, 3], [4, 5, 6]]
print "matrix:", mtrx, "transposed:", zip(*mtrx)

#iterate over multiple lists
for item_a, item_b in zip(list_a, list_b):
    print item_a, item_b

#truncated to shortest
#see itertools.izip_longest for fillvalue with uneven iterables
list_a = ['a', 'b', 'c']
list_b = [0, 1, 2, 3, 4, 5, 6]
print list_a, "and", list_b, "zipped:", zip(list_a, list_b)

#from PSF- The left-to-right evaluation order of the iterables is guaranteed.
#This makes possible an idiom for clustering a data series into n-length groups
#using zip(*[iter(s)]*n).
# the key here is that it is the **same** iterator repeated.  neat!
n = 3
iters = [iter(string.ascii_lowercase)]*n
print zip(*iters)


#all- return true if all items of iterable are true
print all(x[-1] == 'r' for x in months)
#any- return true if any item of iterable is true
print any(x[-1] == 'r' for x in months)


#sorted- return sorted list from iterable
#key is a one arg function that specifies element's comparison key
#see operator.itemgetter
lod = [{'a': 1}, {'a': 0}, {'a': -1}]
print "list:", lod, "sorted via 'a' key:", sorted(lod, key=lambda x: x['a'])
print "reverse sorted:", sorted(lod, key=lambda x: x['a'], reverse=True)

lst = ['a', 'ab', 'c', 'abcd', 'abc', 'a']
print "list:", lst, "sorted by element length:", sorted(lst, key=len)

#with keys sorted
a_dict = {'d': 3, 'a': 0, 'c': 2, 'b': 1}
for key, val in sorted(a_dict.iteritems()):
    print key, val


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

#type to string
print type(a).__name__


#check all elements are of certain type(s)
lst = [1, 2, 3.14, 'hey']
print all(isinstance(x, (int, float, long)) for x in lst)


#next- optional default returned instead of raising StopIteration
#when iterator exhausted
i = iter([42, 2112])
print next(i, 'default')
print next(i, 'default')
print next(i, 'default')


#iter- with two args returns callable-iterator.  first arg is callable, second is a sentinel value.
#when next() called on iterator, callable is called. If val returned by callable does not equal
#sentinel it is returned.  if it does equal sentinel StopIteration is raised.
#https://www.python.org/dev/peps/pep-0234/
for i in iter(lambda: random.randint(1, 7), 3):
    print i, "is not equal to sentinel val of 3"


#sum, min, max
list_a = [1, 2, 3]
list_b = [4, 5, 6]
print sum(itertools.chain(list_a, list_b))
print sum(itertools.chain(list_a, list_b), 10)

lst = ['100', '2', '33']
print min(lst)
#min and max have opt key arg- one arg ordering function
print min(lst, key=lambda x: int(x))

print max(2001, 42, 2112)


#map- apply function to every item of iterable and return list
def double(x):
    return x*2

numbers = [9, 4, 17]
print map(double, numbers)
print map(lambda x: x*2, numbers)


#filter- return list of items of iterable where function returns true
def ends_in_r(x):
    return x[-1] == 'r'

print filter(ends_in_r, months)
print filter(lambda x: x[-1] == 'r', months)
#if function is None then return list of elements that are true
#see itertools.iterfalse to return false elements
print filter(None, [True, 0, 1, [0], {}, (9,)])


#reduce- reduce items of iterable to single val with function with 2 args
#see operator.mul
print range(1, 6), "((((1*2)*3)*4)*5) =", reduce(lambda x, y: x*y, range(1, 6))
