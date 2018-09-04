import itertools


lst_a = [0, 1, 2]
lst_b = ['a', 'b', 'c', 'd']

#typical nested loop
#break only applies to innermost loop
#https://www.python.org/dev/peps/pep-3136/
#https://mail.python.org/pipermail/python-3000/2007-July/008663.html
for a in lst_a:
    for b in lst_b:
        if a == 1 and b == 'c':
            break
        print a, b

print '---'


#single loop using generator expression
for a, b in ((aa, bb) for aa in lst_a for bb in lst_b):
    if a == 1 and b == 'c':
        break
    print a, b

print '---'


#single loop using Cartesian product
for a, b in itertools.product(lst_a, lst_b):
    if a == 1 and b == 'c':
        break
    print a, b
