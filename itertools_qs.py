import calendar
import itertools


astr = 'abc'
num_list = [42, 2001, 2112]
adict = {'key1': 0, 'key2': 1}
months = list(calendar.month_name)[1:]

month_ends_in_r = [m[-1] == 'r' for m in months]
month_ends_in_y = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]


#chain - iterator from multiple iterables
print list(itertools.chain(astr, num_list, adict))


#compress - iterator that returns elements if corresponding
#element in selector arg is true
print list(itertools.compress(months, month_ends_in_r))
print list(itertools.compress(months, month_ends_in_y))


#ifilter
print list(itertools.ifilter(lambda x: x[-1] == 'r', months))
#if predicate is None then return elements that are true
print list(itertools.ifilter(None, [True, 0, 1, [0], {}, (9,)]))

#ifilterfalse - same as ifilter but returns False elements
print list(itertools.ifilterfalse(lambda x: x[-1] == 'r', months))
#if predicate is None then return elements that are false
print list(itertools.ifilterfalse(None, [True, 0, 1, [0], {}, (9,), '']))


#takewhile- returns an iterator that returns elements from iterable
#as long as predicate is true (then stops)
lst = [1, 2, 3, 4, 5, 6, 0, 0, 0]
for val in itertools.takewhile(lambda x: x < 4, lst):
    print val

print '--'

#dropwhile- returns an iterator that returns all remaining elements from iterable
#once predicate is false
for val in itertools.dropwhile(lambda x: x < 4, lst):
    print val


#imap
print list(itertools.imap(lambda x: x*2, num_list))


#islice - negative start/stop/step disallowed
#itertools.islice(iterable, stop)
#itertools.islice(iterable, start, stop[, step])
print list(itertools.islice(months, 3))
print list(itertools.islice(months, 9, None))
print list(itertools.islice(months, 5, 8))
print list(itertools.islice(months, None, None, 2))


#izip - aggregate elements from iterables
print list(itertools.izip('abc', [1, 2, 3], ('i.', 'ii.', 'iii.')))
#izip_longest - iterates over longest iterable in case of uneven len
print list(itertools.izip_longest('abc', [1, 2], ('i.', 'ii.', 'iii.')))
print list(itertools.izip_longest('abc', [1, 2], ('i.', 'ii.', 'iii.'), fillvalue='fv'))


#Cartesian product, permutations, combinations
print list(itertools.product('abc', [42, 2112]))
print list(itertools.permutations('abc'))
print list(itertools.permutations('abc', 2))
print list(itertools.combinations('abc', 2))


#count, cycle, repeat are infinite iterators
#itertools.count(start=0, step=1)
print list(itertools.islice(itertools.count(), 5))
print list(itertools.islice(itertools.count(1, 0.25), 5))

print list(itertools.islice(itertools.cycle('abc'), 7))

#itertools.repeat(object[, times])
print list(itertools.repeat(9, 10))
print list(itertools.islice(itertools.repeat(9), 5))
