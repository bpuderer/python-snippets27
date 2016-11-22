import collections


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


print '---'


# remove from list
lst = [1, 2, 3, 42]
# remove value, ValueError if not present
lst.remove(3)
# remove at index and return, IndexError if empty or out of range
print lst.pop(1)
# if optional index not provided, last item removed/returned
lst.pop()
print lst


print '---'


# clear a list. in python 3, list has a clear method
lst = [1, 2, 3, 4]
print lst
del lst[:]
# lst[:] = [] also works
print "cleared:", lst


print '---'


# shallow copy a list. in python 3, list has a copy method
# see copy module for deep copy
lsta = ['first', 'second', 'third']
#lstb = lsta[:] also works
lstb = list(lsta)
print lstb


print '---'


# reverse a list in place
# also see slicing.py
lst = [0, 1, 2, 3]
print lst, "reversed in place:",
lst.reverse()
print lst


print '---'


# count.  also see collections.Counter
lst = [1, 2, 3, 3, 1, 1]
print "3 occurs", lst.count(3), "times in", lst

lst = [[1, 2], [1, 2, 3, 1, 1], [4, 5]]
print "1 occurs", sum(x.count(1) for x in lst), "times in", lst


print '---'


# http://stackoverflow.com/a/2158532
# http://stackoverflow.com/users/680/cristian
def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el

lst = [[[1, 2, 3], [4, 5, 'abc', (13, (14, 15))]], 6]
print list(flatten(lst))


# docs show example of mutating a list using slicing:
# https://docs.python.org/2.7/tutorial/controlflow.html#for-statements
# from Alex Martelli: http://stackoverflow.com/a/1208792
