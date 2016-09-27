# mutate dict while looping over it
# https://www.youtube.com/watch?v=OSGv2VnC0go#t=19m18s
# don't use    for k in d:
d = {'foo': 0, 'bar': 1, 'baz': 2}
for k in d.keys():
    if k.startswith('ba'):
        del d[k]
print d

# docs show example of mutating a list using slicing:
# https://docs.python.org/2.7/tutorial/controlflow.html#for-statements
# from Alex Martelli: http://stackoverflow.com/a/1208792


# https://www.youtube.com/watch?v=OSGv2VnC0go#t=15m52s
# else clause runs if not interrupted by break or return
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

lst = [9, 7, 3, 42, 2112, 2001]
print find(lst, 13)
print find(lst, 42)


# count.  also see collections.Counter
lst = [1, 2, 3, 3, 1, 1]
tup = (1, 2, 3, 3, 1, 1)
print "3 occurs", lst.count(3), "times in", lst
print "1 occurs", tup.count(1), "times in", tup

lst = [[1, 2], [1, 2, 3, 1, 1], [4, 5]]
print "1 occurs", sum(x.count(1) for x in lst), "times in", lst


# zfill- pad to left with 0's to width
print "'42' with width=5:     ", '42'.zfill(5)
print "'-42' with width=5:    ", '-42'.zfill(5)
print "'Cleese' with width=10:", 'Cleese'.zfill(10)


# str.startswith(prefix[, start[, end]])
# prefix can be a str, unicode or *tuple*
# same for endswith
s = '#abcdef'
print s.startswith('#')
# if s.startswith('#') or s.startswith('/'):
print s.startswith(('#', '/'))


# reverse a list in place
# also see slicing.py
a_list = [0, 1, 2, 3]
print a_list, "reversed in place:",
a_list.reverse()
print a_list


# chained expression
x = 4
if 1 < x < 5:
    print x, 'is between 1 and 5'


# chained assignment
spam = ham = eggs = 42
print spam, ham, eggs


# pass = NOP
pass


# always use is and is not to check for None, never use equality operators
tmp = None
print tmp is None
print tmp is not None


# rename a key in dictionary
a_dict = {'a': 4}
print "original dictionary:", a_dict
# pop raises KeyError if key not in dict and default not provided
a_dict['new_a'] = a_dict.pop('a')
print "'a' renamed to 'new_a':", a_dict


# merge two dictionaries
# better in python3 with PEP 448: https://www.python.org/dev/peps/pep-0448/
# dictc = {**dicta, **dictb}
dicta = {'a': 0, 'b': 1}
dictb = {'b': 2, 'c': 3}
dictc = dicta.copy()
dictc.update(dictb)
print dicta, "and", dictb, "merged:", dictc
