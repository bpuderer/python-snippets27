import itertools


# generators - one result at a time using next
# until exhausted then StopIteration
# NOTE: reverse function just to demo generators
# use built-in reversed() to return a reverse iterator
def reverse(data):
    for idx in range(len(data)-1, -1, -1):
        yield data[idx]

g = reverse('abcd')
print g.next()
for char in g:
    print char


w, x, y, z = reverse('abcd')
print w, x, y, z


# generator expression
data = 'abcd'
g = (data[i] for i in range(len(data)-1, -1, -1))
for char in g:
    print char



# generator with infinite iterator
def divisible_by_nine(nums):
    for n in nums:
        if n % 9 == 0:
            yield n

# first 50 ints starting at 42 that are divisible by 9
print list(itertools.islice(divisible_by_nine(itertools.count(42)), 50))



# https://www.youtube.com/watch?v=EnSu9hHGq5o&t=17m15s
# abstracting the iteration
# from Ned Batchelder
def interesting_lines(f):
    for line in f:
        line = line.strip()
        if line.startswith('#'):
            continue
        if not line:
            continue
        yield line

with open('example.txt') as f:
    for line in interesting_lines(f):
        print 'doing something with:', line
