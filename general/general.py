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


#iteritems
a_dict = {'north': 0, 'south': 1, 'east': 2, 'west': 3}
for key, val in a_dict.iteritems():
    print key, val


#format
print "and {} for {} completely {}".format("now", "something", "different")
print "and {when} for {1} completely {0}".format("different", "something", when="now")
print "{:0>+8.2f}".format(3.14159)


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
