a_str = "Monty Python's Flying Circus"
print "example string:", a_str

#last nth element: seq[-n]
print "last element:", a_str[-1]
print "second to last element", a_str[-2]

#nth element through end: seq[(n-1):]
print "third element through end:", a_str[2:]

#last n elements: seq[-n:]
print "last three elements:", a_str[-3:]

#n elements from beginning: seq[:n]
print "first three elements:", a_str[:3]

#from beginning until(not including) last nth element: seq[:-n]
print "beginning until(not including) third from last element:", a_str[:-3]

#step = -1 reverses sequence
print "reversed:", a_str[::-1]

#step of 2
print "every other element:", a_str[::2]

#elements m through n inclusive: seq[(m-1):n]
print "2nd through 4th inclusive:", a_str[1:4]

#mth to nth to last inclusive: seq[(m-1):-(n-1)]
print "3rd to 2nd to last inclusive:", a_str[2:-1]

#mth to last to nth to last inclusive (wow that sounds awful): seq[-m:-(n-1)]
print "4th to last to 2nd to last inclusive:", a_str[-4:-1]

#naming slices
# https://docs.python.org/2/library/functions.html#slice
#slice(stop)
#slice(start, stop[, step])
first_three_reversed = slice(2, None, -1)
last_three_reversed = slice(None, -4, -1)
print "first three elements reversed:", a_str[first_three_reversed]
print "last three elements reversed:", a_str[last_three_reversed]


#slicing assignment
# insert list items into another list
a_list = ['and', 'something', 'completely', 'different']
a_list[1:1] = ['now', 'for']
print a_list

# replace items in list
a_list = ['and', 'now', 'for', 'everything', 'somewhat', 'different']
a_list[3:5] = ['something', 'completely']
print a_list

#remove items in a list
a_list = ['and', 'now', 'for', 'something', 'this', 'is', 'an', 'ex-parrot', 'completely', 'different']
a_list[4:8] = []
print a_list
