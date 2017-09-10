import random
import sys


# no do-while in python
# https://www.python.org/dev/peps/pep-0315/
# while True:
#    <setup code>
#    if not <condition>:
#        break
#    <loop body>


i = 0
while i != 3:
    print i, "does not equal 3, trying again"
    i = random.randint(0, 5)


print '---'


# https://www.youtube.com/watch?v=OSGv2VnC0go#t=15m52s
# Raymond Hettinger
# same as list.index(x) but -1 instead of ValueError if not found
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


print '---'


# continue - continue with next iteration of loop
for l in "Spam, Spam, Spam, egg and Spam":
    if l == "p":
        continue
    # python3's print function handles this
    # see ../from_future.py
    # print l,  adds a space after each
    sys.stdout.write(l)
print


print '---'


# iteritems- return iterator over (key, val) pairs
# dict.iterkeys(), dict.iteritems(), dict.itervalues() removed from python3
# use keys(), items(), values()
d = {'north': 0, 'south': 1, 'east': 2, 'west': 3}
for key, val in d.iteritems():
    print key, '->', val
