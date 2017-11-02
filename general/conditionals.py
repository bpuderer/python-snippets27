# conditional expression a.k.a. ternary operation was introduced in python 2.5
# https://en.wikipedia.org/wiki/%3F:#Python
# parentheses for readability
# ugly alternatives:
# (False and ['trueval'] or ['falseval'])[0]
# (True and ('trueval',) or ('falseval',))[0]
# ('falseval', 'trueval')[True]
# {True: 'trueval', False: 'falseval'}[False]
# (lambda: 'falseval', lambda: 'trueval')[True]()
print ("trueval" if True else "falseval")
print ("trueval" if False else "falseval")


print '---'


# chained expression
x = 4
if 1 < x < 5:
    print x, "is between 1 and 5"


print '---'


# no switch/case statements in python
# https://www.python.org/dev/peps/pep-3103/
# can also use a dictionary: https://stackoverflow.com/questions/60208/
if x < 0:
    print "negative"
# elif - shortcut for else if
elif x == 0:
    print "is 0"
else:
    print "is positive"


print '---'


# https://docs.python.org/2/reference/expressions.html#boolean-operations
# https://stackoverflow.com/a/17794972
# and/or return last evaluated argument
print '' or 'default'
print '' and 'default'

print 'val' or 'default'
print 'val' and 'default'
