import calendar


# list comprehension
# From PSF docs: A list comprehension consists of brackets containing
# an expression followed by a for clause, then zero or more for or if clauses.
print [i**2 for i in xrange(20) if i % 3 == 0]
print [(x,y) for x in xrange(3) for y in xrange(2)]

# nested list comprehension
print [[(x,y) for x in xrange(3)] for y in xrange(2)]

# parallel list comprehension
print [x for x in zip(xrange(9, 14), xrange(42, 50))]

# list comprehension with conditional expression
words = ['foo', 'bar', 'baz']
print [word.upper() if word.startswith('b') else word for word in words]

# flatten nested list/tuple
# see itertools.chain.from_iterable
lst = [[0, 1], [2, 3], [4], [5, 6]]
tup_of_tups = ((0, 1), (2, 3), (4,), (5, 6))
print [item for sublist in lst for item in sublist]
print [item for subtup in tup_of_tups for item in subtup]


# dictionary comprehensions

# flip keys and values
# same as dict(zip(a_dict.values(), a_dict.keys()))
a_dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3'}
print {v: k for k, v in a_dict.iteritems()}

# dict of even numbers in xrange(14) and their square
print {i: i * i for i in xrange(14) if i % 2 == 0}

# dict of months and whether they end in 'r' or not
print {mth: mth[-1] == 'r' for mth in calendar.month_name[1:]}


# set comprehension

# build set of unique words
words = ['the', 'The', 'THE', 'then', 'Then', 'THEN']
print {word.lower() for word in words}
