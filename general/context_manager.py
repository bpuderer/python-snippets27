# https://www.python.org/dev/peps/pep-0343/
# https://docs.python.org/2/reference/compound_stmts.html#the-with-statement
# http://effbot.org/zone/python-with-statement.htm


class ContextDemo(object):

    def __init__(self):
        print '__init__'

    def __enter__(self):
        print '__enter__'
        return self

    def __exit__(self, ex_type, ex_value, ex_traceback):
        # cleanup, always called
        print '__exit__', ex_type, ex_value
        # return true value to suppress or indicate exception was handled
        # if exception raised and a true value is not returned, exception is re-raised
        return True

    def foo(self):
        print 'foo'
        raise ValueError('ValueError message')

with ContextDemo() as cm:
    # variable after 'as' is assigned the return value of __enter__
    cm.foo()
