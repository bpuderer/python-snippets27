import collections


d = {'a': 0, 'b': 1, 'c': 2, 'd': 3}
del d['b']
# remove key and return value
# KeyError raised if key does not exist and default not provided
print d.pop('c')
print d.pop('x', None)
print d


print '---'


# clear a dictionary
d = {'a': 1, 'b': 2}
print d
d.clear()
print "cleared:", d


print '---'


# iteritems- return iterator over (key, val) pairs
# dict.iterkeys(), dict.iteritems(), dict.itervalues() removed from python3
d = {'north': 0, 'south': 1, 'east': 2, 'west': 3}
for key, val in d.iteritems():
    print key, '->', val


print '---'


# retrieve value when key may or may not exist
# None is returned when key does not exist or optional default val
d = {'a': 1, 'b': 2}
print d.get('c')
print d.get('c', 'default value')

print '-'

# retrieve val and do something with it when key may or may not exist
# good since the 'do something' might not be valid on the default value
# print d.get('c', None)*2  --> TypeError
print (d['c']*3 if 'c' in d else None)
print (d['a']*3 if 'a' in d else None)


print '---'


# setdefault(key[, default])
# can be used to init mutable dict values
# if key in dict, return its val
# if key not in dict, add key, set it to default, and return default
d = {}
d.setdefault('lst', []).append('something')
print d.setdefault('lst', [])
print d.setdefault('lst2')
print d


print '---'


# mutate dict while looping over it
# https://www.youtube.com/watch?v=OSGv2VnC0go#t=19m18s
# don't use    for k in d:
d = {'foo': 0, 'bar': 1, 'baz': 2}
for k in d.keys():
    if k.startswith('ba'):
        del d[k]
print d


print '---'


# rename a key in dictionary
d = {'a': 4}
print d
d['new_a'] = d.pop('a')
print d


print '---'


# merge two dictionaries
# better in python3 with PEP 448: https://www.python.org/dev/peps/pep-0448/
# dictc = {**dicta, **dictb}
dicta = {'a': 0, 'b': 1}
dictb = {'b': 2, 'c': 3}
dictc = dicta.copy()
dictc.update(dictb)
print dicta, "and", dictb, "merged:", dictc


print '---'


# http://stackoverflow.com/a/2158532
# http://stackoverflow.com/users/680/cristian
def walkdict_recur(d, key):
    for k, v in d.iteritems():
        if isinstance(v, collections.Mapping):
            for inner_k, inner_v in walkdict_recur(v, key):
                yield inner_k, inner_v
        else:
            if k == key:
                yield k, v

# http://stackoverflow.com/a/10757107
# http://stackoverflow.com/users/166749/fred-foo
def walkdict_iter(d, key):
    stack = d.items()
    while stack:
        k, v = stack.pop()
        if isinstance(v, dict):
            stack.extend(v.iteritems())
        else:
            if k == key:
                yield v

d = {'z': 99, 'a': {'aa': {'aaa': 2}}, 'b': 12, 'aaa': "abc", 'y': {'yy': {'yyy': 4}}}
print list(walkdict_recur(d, 'aaa'))
print list(walkdict_iter(d, 'aaa'))
