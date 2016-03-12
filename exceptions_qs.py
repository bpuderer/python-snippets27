# catch all exceptions, generally not a good idea
try:
    raise KeyboardInterrupt
except:
    print "an exception was raised"

print "-----"


# multiple except clauses
try:
    raise AssertionError('AssertionError message')
except ValueError as e:
    print e
except AssertionError as e:
    print e

print "-----"


# multiple exceptions for except clause
try:
    raise ValueError('ValueError message')
except (AssertionError, ValueError) as e:
    print e

print "-----"


# else and finally
try:
    raise TypeError('TypeError message')
except TypeError:
    print "problem with type"
else:
    #executes if try clause does not raise an exception
    print "in else"
finally:
    #always executed before leaving the try statement
    print "in finally"

print "-----"


# same as previous example except try clause does not raise an exception
try:
    pass
except TypeError as e:
    print e
else:
    print "in else"
finally:
    print "in finally"

print "-----"


# raise with no arguments re-raises the last exception
# used to identify exception was raised but won't handle it
# in this example, the raise will cause the script to exit
try:
    raise RuntimeError('message from RuntimeError')
except RuntimeError:
    print "RuntimeError happened but I'm not handling it"
    raise
