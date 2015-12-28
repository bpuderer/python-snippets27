import random
import string

#int
print "random int between 0 and 5 inclusive:", random.randint(0, 5)
print "random int in range(5):", random.randrange(5)
print "random int in range(4, 37, 8):", random.randrange(4, 37, 8)


#float
print "random float in [0.0, 1.0):", random.random()
print "random float using a=2, b=4 in a + (b-a) * random():", random.uniform(2, 4)


#sequence
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
print "pick random element in sequence of months:", random.choice(months)
print "random lowercase ascii letter:", random.choice(string.ascii_lowercase)

some_numbers = [1, 2, 3, 4, 5]
print "some numbers before shuffling them:", some_numbers
random.shuffle(some_numbers)
print "some numbers after shuffling them in place:", some_numbers

print "sample three months:", random.sample(months, 3)

print "Notes about sampling:"
print "Population sampled is not modified. Returned list is in selection order."
print "Population is NOT REQUIRED to contain unique elements."
print "Each element in poplulation, unique or not, may be returned (once)."
print "Here are 10 samples of size 3 where population = [0, 1, 1, 0, 1] to demo"
for i in range(10):
    print random.sample([0, 1, 1, 0, 1], 3)
