from collections import namedtuple
from string import Template


# format
movie = {'title': 'Life of Brian', 'director': 'Terry Jones', 'year': 1979}
words = ['now', 'something', 'different']
print "{title} directed by {director} was released in {year}".format(**movie)
print "{0[title]} directed by {0[director]} was released in {0[year]}".format(movie)
print "and {} for {} completely {}".format(*words)
print "and {} for {} completely {}".format("now", "something", "different")
print "and {when} for {1} completely {0}".format("different", "something", when="now")
print "and {0[0]} for {0[1]} completely {0[2]}".format(words)

print "use doubling to include curly brace {}: {{ }}".format("chars")

print "{:0>+8.2f}".format(3.14159)

Point = namedtuple('Point', ['x', 'y'])
p = Point(x=-1.0, y=-2.0)
print "x={0.x} y={0.y}".format(p)

class SomeClass(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

c = SomeClass()
print '{cls!s} {cls!r}'.format(cls=c)


print '---'


# concat strings in iterable using separator
print '-'.join('abcd')
# https://stackoverflow.com/a/9061024
# list comprehension faster and more memory efficient than
# generator expression for str.join
print ''.join([str(i) for i in xrange(10)])


print '---'


t = Template("Hello my name is $name")
# substitute(mapping[, **kws])
# KeyError if placeholder missing from mapping
print t.substitute(name="Aloysius")
# no KeyError with safe_substitute if placeholder...
print t.safe_substitute(foo="bar")


print '---'


# zfill- pad to left with 0's to width
print "'42' with width=5:     ", '42'.zfill(5)
print "'-42' with width=5:    ", '-42'.zfill(5)
print "'Cleese' with width=10:", 'Cleese'.zfill(10)


print '---'


# str.startswith(prefix[, start[, end]])
# prefix can be a str, unicode or *tuple*
# same for endswith
s = '#abcdef'
print s.startswith('#')
# if s.startswith('#') or s.startswith('/'):
print s.startswith(('#', '/'))


print '---'


# string.rstrip(s[, chars])
# characters in chars string stripped from end
print '/resource/z/z/z/z'.rstrip('/z')
print '/resource'.rstrip('/')


# strip string from ending of another string
astring = "ZZZZ blah blah blah ZZZ"
ending = "ZZZ"
if astring.endswith(ending):
    print astring[:-len(ending)]
