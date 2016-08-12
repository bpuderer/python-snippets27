# unpacking sequences
lst = [0, 'abc', [1, 2]]
a, b, c = lst
print a, b, c

a, b, (c, d) = lst
print a, b, c, d

# in python3- a, *b = c
# https://www.python.org/dev/peps/pep-3132/
c = [1, 2, 3]
a, b = c[0], c[1:]
print a, b

c = (1, 2, 3)
a, b = c[0], c[1:]
print a, b


# simultaneous updates
a, b = 1, 2
print a, b
a, b = b, a
print "swapped:", a, b

a, b = 1, 2
print a, b
a, b = b, a+b
print "a gets b and b gets a+b:", a, b


# conditional expression a.k.a. ternary operation was introduced in python 2.5
# https://en.wikipedia.org/wiki/%3F:#Python
# parentheses for readability
# ugly alternatives:
# (False and ['trueval'] or ['falseval'])[0]
# (True and ('trueval',) or ('falseval',))[0]
# ('falseval', 'trueval')[True]
# {True: 'trueval', False: 'falseval'}[False]
# (lambda: 'falseval', lambda: 'trueval')[True]()
x = ('trueval' if True else 'falseval')
print x


# clear a list
a_list = [1, 2, 3, 4]
print "a_list:", a_list
del a_list[:]
# a_list[:] = [] also ok
print "a_list cleared:", a_list


# clear a dictionary
a_dict = {'a': 1, 'b': 2}
print "a_dict:", a_dict
a_dict.clear()
print "a_dict cleared:", a_dict


# iteritems- return iterator over (key, val) pairs
# dict.iterkeys(), dict.iteritems(), dict.itervalues() removed from python3
a_dict = {'north': 0, 'south': 1, 'east': 2, 'west': 3}
for key, val in a_dict.iteritems():
    print key, '->', val


# retrieve value when key may or may not exist
# None is returned when key does not exist or optional default val
a_dict = {'a': 1, 'b': 2}
print a_dict.get('c')
print a_dict.get('c', 'default value')

# retrieve val and do something with it when key may or may not exist
# good since the 'do something' might not be valid on the default value
# print a_dict.get('c', None)*2  --> TypeError
print (a_dict['c']*3 if 'c' in a_dict else None)
print (a_dict['a']*3 if 'a' in a_dict else None)


# setdefault(key[, default])
# can be used to init mutable dict values
# if key in dict, return its val
# if key not in dict, add key, set it to default, and return default
a_dict = {}
a_dict.setdefault('lst', []).append('something')
print a_dict.setdefault('lst', [])
print a_dict.setdefault('lst2')
print a_dict


# rename a key in dictionary
a_dict = {'a': 4}
print "original dictionary:", a_dict
# pop raises KeyError if key not in dict and default not provided
a_dict['new_a'] = a_dict.pop('a')
print "'a' renamed to 'new_a':", a_dict


# add to list
lst = [0, 1]
# append object to end
lst.append(2)
# extend list by appending elements from iterable
lst.extend([3, 4])
# insert object before index
lst.insert(2, "insert this before element at index 2")
# see careful.py
lst += [5]
print lst


# format
movie = {'title': 'Life of Brian', 'director': 'Terry Jones', 'year': 1979}
words = ['now', 'something', 'different']
print "{title} directed by {director} was released in {year}".format(**movie)
print "and {} for {} completely {}".format(*words)
print "and {} for {} completely {}".format("now", "something", "different")
print "and {when} for {1} completely {0}".format("different", "something", when="now")
print "{:0>+8.2f}".format(3.14159)
