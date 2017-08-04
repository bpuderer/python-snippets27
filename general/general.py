# sequence unpacking
lst = [0, 'abc', [1, 2]]
a, b, c = lst
print a, b, c

a, b, (c, d) = lst
print a, b, c, d


print '---'


# in python3- a, *b = c
# https://www.python.org/dev/peps/pep-3132/
c = "unpack"
a, b = c[0], c[1:]
print a, b


print '---'


# simultaneous updates
a, b = 1, 2
print a, b
a, b = b, a
print "swapped:", a, b

print '-'

a, b = 4, 2
print a, b
a, b = b, a+b
print "a gets b and b gets a+b:", a, b


print '---'


# chained assignment
spam = ham = eggs = 42
print spam, ham, eggs


print '---'


# pass = NOP/NOOP
pass


print '---'


# always use is and is not to check for None, never use equality operators
tmp = None
print tmp is None
print tmp is not None


# use [] and {} instead of list() and dict()
# https://stackoverflow.com/a/30216156
