from __future__ import print_function
import sys


# print(*objects, sep=' ', end='\n', file=sys.stdout)
print('spam', 'wonderful spam')
print('spam', 'wonderful spam', sep=', ')
print('spam', 'wonderful spam', sep=', ', end=' FIN\n')
print('stderr', 'spam', 'wonderful spam', sep=', ', end=' FIN\n', file=sys.stderr)
