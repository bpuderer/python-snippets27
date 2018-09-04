import copy


# shallow copy
lista = [0, 1, 2]
#listb = lista[:]
#listb = list(lista)
listb = copy.copy(lista)
lista.append(3)
print lista
print listb
print "---"

# deep copy
lista = [[0, 1], [2, 3], 4]
listb = copy.deepcopy(lista)
lista[0].append(5)
print lista
print listb
print "---"

# shallow copy
dicta = {'a': 0, 'b': 1}
#dictb = dict(dicta)
dictb = copy.copy(dicta)
dicta['c'] = 2
print dicta
print dictb
print "---"

# deep copy
dicta = {'a': {'aa': 0}, 'b': 1}
dictb = copy.deepcopy(dicta)
dicta['a']['aaa'] = 2
print dicta
print dictb
print "---"
