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


# conditional expression a.k.a. ternary operation was introduced in python 2.5
# https://en.wikipedia.org/wiki/%3F:#Python
# parentheses for readability
# ugly alternatives:
# (False and ['trueval'] or ['falseval'])[0]
# (True and ('trueval',) or ('falseval',))[0]
# ('falseval', 'trueval')[True]
# {True: 'trueval', False: 'falseval'}[False]
# (lambda: 'falseval', lambda: 'trueval')[True]()
print ('trueval' if True else 'falseval')
print ('trueval' if False else 'falseval')

print '---'


# chained expression
x = 4
if 1 < x < 5:
    print x, 'is between 1 and 5'


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


print '---'


# https://www.youtube.com/watch?v=OSGv2VnC0go#t=15m52s
# else clause runs if not interrupted by break or return
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

lst = [9, 7, 3, 42, 2112, 2001]
print find(lst, 13)
print find(lst, 42)
