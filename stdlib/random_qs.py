import random
import string
import calendar


#int
print "random int between 0 and 5 inclusive:", random.randint(0, 5)
print "random month:", calendar.month_name[random.randint(1, 12)]
print "random int in range(5):", random.randrange(5)
print "random int in range(4, 37, 8):", random.randrange(4, 37, 8)


#float
print "random float in [0.0, 1.0):", random.random()
print "random float in [1.21, 3.14]:", random.uniform(1.21, 3.14)

#sequence
players = ['Jackson', 'Johnson', 'Mills', 'Swilling', 'Brees', 'Hebert', 'Mora', 'Manning', 'Andersen', 'McAllister', 'Colston', 'Heyward', 'Porter', 'Roaf', 'Morstead', 'Dempsey', 'Hilliard', 'Mayes']
print "pick random element in sequence of players:", random.choice(players)
print "random lowercase ascii letter:", random.choice(string.ascii_lowercase)

some_numbers = range(10)
print "list of numbers:", some_numbers
random.shuffle(some_numbers)
print "list after shuffling in place:", some_numbers

print "sample five players:", random.sample(players, 5)

print "Notes about sampling:"
print "Population sampled is not modified. Returned list is in selection order."
print "Population is NOT REQUIRED to contain unique elements."
print "Each element in poplulation, unique or not, may be returned (once)."
print "Here are 10 samples of size 3 where population = [0, 1, 1, 0, 1] to demo"
for i in range(10):
    print random.sample([0, 1, 1, 0, 1], 3)
