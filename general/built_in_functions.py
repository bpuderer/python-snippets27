import calendar
import itertools
import operator
import random
import string


months = calendar.month_name[1:]


#enumerate
print list(enumerate("abcdefg"))
print list(enumerate("abcdefg", start=2))

cardinal_directions = ['north', 'south', 'east', 'west']
for idx, direction in enumerate(cardinal_directions):
    print idx, direction


#range and xrange
#xrange renamed to range in python 3
#to gen a list with range in python 3: list(range(n))
print range(10, 0, -2)

print type(xrange(10, 0, -2))
for i in xrange(10, 0, -2):
    print i


#zip- from PSF- returns list of tuples where the i-th tuple contains
#the i-th element from each of the argument sequences or iterables.
#The returned list is truncated in length to the length of the shortest argument sequence.
#in python 3, zip returns an iterator instead of a list
#https://en.wikipedia.org/wiki/Convolution_(computer_science)
list_a = ['a', 'b', 'c']
list_b = [0, 1, 2]
zipped = zip(list_a, list_b)
print list_a, "and", list_b, "zipped:", zipped
#see itertools.izip
print "to dictionary:", dict(zip(list_a, list_b))
print "unzipped:", zip(*zipped)

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

mtrx = [[1, 2, 3], [4, 5, 6]]
print "matrix:", mtrx, "transposed:", zip(*mtrx)

#swap keys and values. see comprehensions.py for better solution
#values and keys correspond: https://docs.python.org/2.7/library/stdtypes.html#dict.items
a_dict = {'a': 0, 'b': 1, 'c': 2}
print "keys and vals swapped:", dict(zip(a_dict.values(), a_dict.keys()))


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
print min(lst, key=int)

print max(2001, 42, 2112)

prices = {'MSFT': 57.18, 'AAPL': 105.63, 'FB': 124.24,
          'AMZN': 762.96, 'GOOG': 772.58, 'IBM': 160.93}
print min(prices.keys(), key=prices.get)
print min(prices.iteritems(), key=operator.itemgetter(1))

print max(prices.keys(), key=prices.get)
print max(prices.iteritems(), key=operator.itemgetter(1))

print sorted(prices.keys(), key=prices.get)
print sorted(prices.iteritems(), key=operator.itemgetter(1))


#all- return true if all items of iterable are true
print all(x[-1] == 'r' for x in months)
#any- return true if any item of iterable is true
print any(x[-1] == 'r' for x in months)


#sorted(iterable[, cmp[, key[, reverse]]]) return sorted list from iterable
#key is a one arg function that specifies element's comparison key
#cmp specifies a two arg custom comparison function that returns +n, 0, -n
#cmp removed in python 3
#https://www.youtube.com/watch?v=OSGv2VnC0go&t=10m05s
lod = [{'a': 1}, {'a': 0}, {'a': -1}]
print "list:", lod, "sorted via 'a' key:", sorted(lod, key=operator.itemgetter('a'))
print "reverse sorted:", sorted(lod, key=operator.itemgetter('a'), reverse=True)

lst = ['a', 'ab', 'c', 'abcd', 'abc', 'a']
print "list:", lst, "sorted by element length:", sorted(lst, key=len)

#with keys sorted
a_dict = {'d': 3, 'a': 0, 'c': 2, 'b': 1}
for key, val in sorted(a_dict.iteritems()):
    print key, val


#loop backwards
lst = ['first', 'second', 'third']
for item in reversed(lst):
    print item


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
print range(1, 6), "((((1*2)*3)*4)*5) =", reduce(operator.mul, range(1, 6))
