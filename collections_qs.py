import itertools
from collections import defaultdict, OrderedDict, Counter, namedtuple, deque


# defaultdict can define default_factory where
# accessing a key which does not exist, creates it with a default value
# and the default value is returned
# commonly used to append to lists in dictionaries

dd1 = defaultdict(list)
print dd1
print dd1['addme']
print dd1
print dict(dd1)

print '---'

# grouping idiom
names = ['van Rossum', 'torvalds', 'stallman', 'thompson', 'ritchie', 'wall', 'gosling']

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print d

print '---'

# defaultdict inside defaultdict...
# trees, json
# https://gist.github.com/hrldcpr/2012250
# https://www.youtube.com/watch?v=uWGPxYDo87Q#t=14m35s

dd2 = defaultdict(lambda: defaultdict(dict))
print dd2
print dd2['lev1']['lev2']
print dd2

print '---'


# Counter - unordered collection where elements are dict keys
# and their counts are stored as dict values

c = Counter('these are attack eyebrows.')
print c
print "t occurs", c['t'], "times"
#0 returned for missing items instead of KeyError as with dict
print "z occurs", c['z'], "times"
print "Top two most common:", c.most_common(2)
print "appear more than once:", [k for k, v in c.iteritems() if v > 1]
#elements returns iterator
print "elements:", list(c.elements())
del c['t']
print "after 't' removed:", c
print '-'

# with generator
print Counter(len(name) for name in names)
print '-'

# nested
lst = [[1, 2, 1], [2, 3, 1, 1], [], [4, 5]]
print Counter(itertools.chain(*lst))
#print Counter(val for sub in lst for val in sub)
print '-'

# other ways to init
print Counter({'a': 4, 'b': 3})
print Counter(a=4, b=3)

print '---'


# namedtuple- tuple subclass, uses no more memory than regular tuple
# "you should use named tuples instead of tuples anywhere you think object notation
#  will make your code more pythonic and more easily readable"
# http://stackoverflow.com/a/2970722

# fieldnames specified as a sequence of strings
# can also specify fieldnames as single string with fieldnames separated by
# whitespace and/or commas
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1.0, 2.0)
p2 = Point(x=-1.0, y=-2.0)
print p1
print p2
print p1.x, p1[1]
print p2.x, p2.y

print '-'

# Raymond Hettinger, author of namedtuple on 'clarifying
# multiple return values with named tuples':
# https://www.youtube.com/watch?v=OSGv2VnC0go&t=32m19s
def get_name():
    name = namedtuple("name", ["first", "middle", "last"])
    return name("John", "Marwood", "Cleese")

name = get_name()
print name.first, name.middle, name.last

print '---'


# deque - pronounced 'deck', thread-safe
d = deque('efg')
d.append('h')
d.appendleft('d')
print d
# extend and extendleft take an iterable
d.extend('ijk')
# left appends in the arg in reverse order to the front
d.extendleft('cba')
print d
print d.pop()
print d.popleft()
print d
d.remove('i')
print d

# when new items are added beyond maxlen an equal number
# are removed from the opposite end
d = deque(maxlen=3)
d.extend('abc')
print d
d.append('d')
print d
d.appendleft('a')
print d

print '---'


# OrderedDict - dictionary that preserves the order keys were added

od1 = OrderedDict()
od1['a'] = 0
od1['b'] = 1
od1['c'] = 2
od1['d'] = 3
print od1

a_dict = {}
a_dict['a'] = 0
a_dict['b'] = 1
a_dict['c'] = 2
a_dict['d'] = 3
print a_dict
