import heapq
import operator


#heapq.nlargest(n, iterable[, key])
#heapq.nsmallest(n, iterable[, key])
lst = [1, 2001, 42, 9, 2010, 2112, 7, 1776]
print heapq.nlargest(3, lst)
print heapq.nsmallest(2, lst)

#with key
lst = [{'id': 0, 'val': 9}, {'id': 1, 'val': 2112}, {'id': 2, 'val': 2001},
       {'id': 3, 'val': 2010}, {'id': 4, 'val': 42}, {'id': 5, 'val': 13}]
print heapq.nlargest(2, lst, key=operator.itemgetter('val'))


#heapq.merge(*iterables)
#docs: "Similar to sorted(itertools.chain(*iterables)) but returns an iterable"
lst_a = [13, 1776, 42]
lst_b = [-10, 9, 2001]
print list(heapq.merge(lst_a, lst_b))
