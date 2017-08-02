import collections


# adding...
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


# removing...
lst = [1, 2, 3, 42, 28, 3]
# remove value, ValueError if not present
lst.remove(3)
# remove at index and return, IndexError if empty or out of range
print lst.pop(1)
# if optional index not provided, last item removed/returned
lst.pop()
# remove element at index
del lst[0]
print lst


print '---'


# ValueError if item not in list
lst = [28, 3, 9, 42]
print "index of 9 in list is", lst.index(9)


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
lst = [44, 17, 23, 3, 19]
print lst, "reversed in place:",
lst.reverse()
print lst

# list.sort(cmp=None, key=None, reverse=False)
# see ../operator_qs.py
lst.sort()
print "sorted in place:", lst


print '---'


# remove duplicates from list, maintain order
# see ../collections_qs.py
# https://stackoverflow.com/a/7961425


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
