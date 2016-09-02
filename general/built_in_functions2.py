import calendar


#prompt for input
user_input = ''
while not user_input:
    user_input = raw_input("Enter something so we can move on: ")
print "You entered:", user_input


#bin, hex, oct, format
n = 42
print n, 'in binary is', bin(n), 'and', format(n, 'b'), 'sans prefix'
print n, 'in hex is', hex(n), 'and', format(n, 'x'), 'sans prefix'
print n, 'in octal is', oct(n), 'and', format(n, 'o'), 'sans prefix'


#isinstance
class Test1(object):
    pass

class Test2(Test1):
    pass

a = Test1()
b = Test2()

print "Test2 is derived from Test1.  a is instance of Test1, b is instance of Test2"

print "type(a) is Test1:", type(a) is Test1
print "type(b) is Test1:", type(b) is Test1
print "type(a) is Test2:", type(a) is Test2
print "type(b) is Test2:", type(b) is Test2
print "isinstance(a, Test1):", isinstance(a, Test1)
print "isinstance(b, Test1):", isinstance(b, Test1)
print "isinstance(a, Test2):", isinstance(a, Test2)
print "isinstance(b, Test2):", isinstance(b, Test2)

#type to string
print type(a).__name__

#check all elements are of certain type(s)
lst = [1, 2, 3.14, 'hey']
print all(isinstance(x, (int, float, long)) for x in lst)

#cmp
print "cmp(x, y) returns", cmp(42, 22), "when x > y"
print "cmp(x, y) returns", cmp(22, 42), "when x < y"
print "cmp(x, y) returns", cmp(42, 42), "when x == y"

#dir
print dir()
print dir({})
print dir(list)
print dir(calendar)
