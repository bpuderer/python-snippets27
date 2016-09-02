import calendar


# list comprehension
# From PSF docs: A list comprehension consists of brackets containing
# an expression followed by a for clause, then zero or more for or if clauses.
print [i**2 for i in xrange(20) if i % 3 == 0]
print [(x,y) for x in xrange(3) for y in xrange(2)]

# nested list comprehension
print [[(x,y) for x in xrange(3)] for y in xrange(2)]

# any/all with list comprehension
restaurants = ["Pontchartrain Po-Boys", "Don's Seafood", "Acme Oyster House",
               "DiCristina's Restaurant", "DiMartino's Muffulettas", "Mandeville Seafood",
               "Bear's Restaurant", "Pat's Seafood & Cajun Deli",
               "Buster's Place Restaurant and Oyster Bar", "Abita Brew Pub"]
names = ["seafood", "po-boy"]
print [rest for rest in restaurants if any(name.lower() in rest.lower() for name in names)]

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
