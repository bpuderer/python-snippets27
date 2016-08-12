# http://pythontutor.com/



# mutable default args
def append_to(element, alist=[]):
    # default args are only evaluated when defined, not
    # each time it is called
    alist.append(element)
    return alist

print append_to(42)
print "???", append_to(2112)


def append_to2(element, alist=None):
    # typical solution
    if alist is None:
        alist = []
    alist.append(element)
    return alist

print append_to2(42)
print append_to2(2112)



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



# one item tuples need a trailing comma
a = (3)
print a, type(a)
b = (3,)
print b, type(b)



# multiple exceptions for a single except clause
# requires a parenthesized tuple
try:
    raise ValueError('ValueError message')
except (AssertionError, ValueError) as e:
    print e



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
