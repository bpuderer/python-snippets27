import calendar


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


# list comprehension
print [i**2 for i in xrange(20) if i % 3 == 0]
print [(x,y) for x in xrange(3) for y in xrange(2)]

# nested list comprehension
print [[(x,y) for x in xrange(3)] for y in xrange(2)]
