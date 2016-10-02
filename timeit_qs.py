"""timeit to compare flattening a list algorithms"""

import timeit


# python -m timeit [-n N] [-r N] [-s S] [-t] [-c] [-h] [statement ...]
# python -m timeit -s 'l=[[1,2,3,4],[5,6],[7],[8,9]]*25' '[item for sublist in l for item in sublist]'


# timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)
print timeit.timeit("list(itertools.chain.from_iterable(l))",
                    setup="import itertools; l=[[1,2,3,4],[5,6],[7],[8,9]]*25")

print timeit.timeit("[item for sub in l for item in sub]",
                    setup="l=[[1,2,3,4],[5,6],[7],[8,9]]*25")

print timeit.timeit("reduce(operator.add, l)",
                    setup="import operator; l=[[1,2,3,4],[5,6],[7],[8,9]]*25")

print timeit.timeit("sum(l, [])",
                    setup="l=[[1,2,3,4],[5,6],[7],[8,9]]*25")
