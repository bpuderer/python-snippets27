# args is a tuple, kwargs is a dictionary
def some_function(a, b, c=0, d=1, *args, **kwargs):
    print "a:", a, "b:", b, "c:", c, "d:", d, "args:", args, "kwargs:", kwargs


print "def some_function(a, b, c=0, d=1, *args, **kwargs):"

print "---"

print "some_function(11, 12)"
some_function(11, 12)

print "---"

print "some_function(11, 12, d=5)"
some_function(11, 12, d=5)

print "---"

print "some_function(11, 12, 13, 14, 15, 16)"
some_function(11, 12, 13, 14, 15, 16)

print "---"

print "some_function(11, 12, e=2)"
some_function(11, 12, e=2)

print "---"

print "a_dict = {'c': 10, 'abc': 123, 'xyz': 321}"
print "some_function(11, 12, **a_dict)"
a_dict = {'c': 10, 'abc': 123, 'xyz': 321}
some_function(11, 12, **a_dict)

print "---"

print "a_dict = {'z': 999, 'a': 11, 'b': 12}"
print "some_function(**a_dict)"
a_dict = {'z': 999, 'a': 11, 'b': 12}
some_function(**a_dict)

print "---"

print "a_list = [11, 12, 13]"
print "some_function(*a_list)"
a_list = [11, 12, 13]
some_function(*a_list)

print "---"

print "a_tuple = (11, 12, 13, 14, 15, 16)"
print "some_function(*a_tuple)"
a_tuple = (11, 12, 13, 14, 15, 16)
some_function(*a_tuple)
