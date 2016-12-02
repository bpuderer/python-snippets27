# http://pythontutor.com/
import time


# mutable default args
def append_to(element, lst=[]):
    # default args are only evaluated when defined, not each call
    lst.append(element)
    return lst

print append_to(42)
print "???", append_to(2112)

print '-'

# typical solution
def append_to_fixed(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst

print append_to_fixed(42)
print append_to_fixed(2112)

print '-'

# another demo of default args only evaluated when defined
print "current time:", time.time()
time.sleep(1)
print "defining print_time()..."
def print_time(t=time.time()):
    print "in print_time():", t
time.sleep(1)
print "current time:", time.time()
time.sleep(1)
print_time()
time.sleep(1)
print_time()


print '---'


# don't use mutable class variables
class Foo(object):
    bar = []

    def add(self, baz):
        self.bar.append(baz)

f1 = Foo()
f2 = Foo()
f1.add('spam')
print 'f1.bar:', f1.bar
print 'f2.bar:', f2.bar, '???'


print '---'


# global statement
bar = 42
def foo():
    # w/o global:
    # UnboundLocalError: local variable 'bar' referenced before assignment
    global bar
    bar += 1

foo()
print bar

a_list = [1, 2, 3]
a_dict = {'key1': 'val1'}
def foo2():
    a_list.append(4)
    a_dict['key2'] = 'val2'

foo2()
print a_list
print a_dict

baz = 8
def foo3():
    baz = 9
    print baz

foo3()
print baz


print '---'


# one item tuples need a trailing comma
a = (3)
print a, type(a)
b = (3,)
print b, type(b)


print '---'


# multiple exceptions for a single except clause
# requires a parenthesized tuple
try:
    raise ValueError('ValueError message')
except (AssertionError, ValueError) as e:
    print e


print '---'


# careful with + and lists
a = [1, 2]
b = a
a.append(3)
a.extend([4, 5])
# modifies existing list object
a += [6]
# creates a new list object!
a = a + [7]
print "a:", a, "b:", b


print '---'


# init 2-D matrix
# not good. each 'row list' references the same list object
board = [[0]*4]*4
board[0][0] = 42
print board

# better
board = [[0]*4 for _ in range(4)]
#board = [[0 for _ in range(4)] for _ in range(4)]
board[0][0] = 42
print board


print '---'


# careful with mutables and chained assignment
x = y = []
x += [18]
x.append(22)
print x
print y, 'uh oh'


print '---'


# https://docs.python.org/2/reference/expressions.html#generator-expressions
# https://www.python.org/dev/peps/pep-0289/#early-binding-versus-late-binding
# "the first (outermost) for-expression should be evaluated immediately and that the remaining
# expressions be evaluated when the generator is executed."
lst1 = [0, 1]
lst2 = [10, 20]
g = (i+j for i in lst1 for j in lst2)
lst1 = [1, 2]
lst2 = [100, 200]
print g.next()
