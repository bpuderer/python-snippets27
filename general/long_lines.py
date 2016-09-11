""" PEP 8:
The preferred way of wrapping long lines is by using Python's implied
line continuation inside parentheses, brackets and braces.
https://www.python.org/dev/peps/pep-0008/#maximum-line-length
"""

# break *before* binary operator preferred for readability
print (1
       + 2
       + 3)

print range(1,
            10,
            2)

print [1, 2,
       3]

print {'a': 0,
       'b': 1}

print ("a really really"
       " not really long"
       " string")

print ("string format example {} {}".
       format("str1", "str2"))

if (True
        or False
        or True):
    print "something"


# PEP 8: Backslashes may still be appropriate at times.
# explicit line continuation
# \ must be last character on line, else SyntaxError
print 1 + 2 \
      + 3
