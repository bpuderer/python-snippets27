#clear a list
a_list = [1, 2, 3, 4]
print "a_list:", a_list
del a_list[:]
#a_list[:] = [] also ok
print "a_list cleared:", a_list


#clear a dictionary
a_dict = {'a': 1, 'b': 2}
print "a_dict:", a_dict
a_dict.clear()
print "a_dict cleared:", a_dict

#retrieve value when key may or may not exist
#None is returned when key does not exist or optional default val
print a_dict.get('c')
print a_dict.get('c', 'default value')

#rename a key in dictionary
a_dict = {'a': 0}
print "orig dict:", a_dict
#pop raises KeyError if key not in dict and default not provided
a_dict['new_a'] = a_dict.pop('a')
print "'a' renamed to 'new_a':", a_dict

#iteritems
a_dict = {'north': 0, 'south': 1, 'east': 2, 'west': 3}
for key, val in a_dict.iteritems():
    print key, val


#format
movie = {'title': 'Life of Brian', 'director': 'Terry Jones', 'year': 1979}
words = ['now', 'something', 'different']
print "{title} directed by {director} was released in {year}".format(**movie)
print "and {} for {} completely {}".format(*words)
print "and {} for {} completely {}".format("now", "something", "different")
print "and {when} for {1} completely {0}".format("different", "something", when="now")
print "{:0>+8.2f}".format(3.14159)


#str.startswith(prefix[, start[, end]])
#prefix can be a str, unicode or *tuple*
#same for endswith
s = '#abcdef'
print s.startswith('#')
#if s.startswith('#') or s.startswith('/'):
print s.startswith(('#', '/'))


#reverse a list in place
#also see slicing.py
a_list = [0, 1, 2, 3]
print a_list, "reversed in place:",
a_list.reverse()
print a_list


#always use is and is not to check for None, never use equality operators
tmp = None
print tmp is None
print tmp is not None


#unpacking an iterable
lst = [0, 'abc', [1, 2]]
a, b, c = lst
print a, b, c

a, b, (c, d) = lst
print a, b, c, d

a, b = 1, 2
print a, b
a, b = b, a
print "swapped:", a, b


#chained expression
x = 4
if 1 < x < 5:
    print x, 'is between 1 and 5'


#conditional expression
#parentheses for readability, not required
x = (42 if True else 2001)
print x
x = 42 if False else 2001
print x


#setdefault(key[, default])
#can be used to init mutable dict values
#if key in dict, return its val
#if key not in dict, add key, set it to default, and return default
a_dict = {}
a_dict.setdefault('lst', []).append('something')
print a_dict.setdefault('lst', [])
print a_dict.setdefault('lst2')
print a_dict
