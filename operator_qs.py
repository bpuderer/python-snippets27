import operator


#https://docs.python.org/2/library/operator.html#mapping-operators-to-functions

numbers = [9, 4, 17]
#print map(lambda x: -x, numbers)
print map(operator.neg, numbers)

#print range(1, 6), "((((1*2)*3)*4)*5) =", reduce(lambda x, y: x*y, range(1, 6))
print range(1, 6), "((((1*2)*3)*4)*5) =", reduce(operator.mul, range(1, 6))



#attrgetter
class MyClass:
    def __init__(self, val):
        self.val = val

    def inc_val(self):
        self.val += 1

    def add_to_val(self, n):
        self.val += n

lst = [MyClass(2001), MyClass(0), MyClass(42), MyClass(9)]

#lst.sort(key=lambda x: x.val)
lst.sort(key=operator.attrgetter('val'))
print [i.val for i in lst]


#methodcaller
#map(MyClass.inc_val, lst)
map(operator.methodcaller('inc_val'), lst)
print [i.val for i in lst]

map(operator.methodcaller('add_to_val', 3), lst)
print [i.val for i in lst]


#itemgetter
lst = [{'a': 2001, 'b': 0}, {'a': 0, 'b': 2112}, {'a': 0, 'b': 2001},
       {'a': 0, 'b': 2010}, {'a': 42, 'b': 999}, {'a': 9, 'b': 0}]
#lst.sort(key=lambda x: x['a'])
lst.sort(key=operator.itemgetter('a'))
print "\nsorted on just 'a' key:\n", lst

#lst.sort(key=lambda x: (x['a'], x['b']))
lst.sort(key=operator.itemgetter('a', 'b'))
print "\nsorted on 'a' and 'b' keys:\n", lst


lst = [(2001, 0), (0, 2112), (0, 2001), (0, 2010), (42, 0), (9, 0)]
#lst.sort(key=lambda x: x[0])
lst.sort(key=operator.itemgetter(0))
print "\nsorted on first element in tuple:\n", lst
