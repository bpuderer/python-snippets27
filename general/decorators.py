import operator
import time

# https://www.python.org/dev/peps/pep-0318/

def log_args(func):
    def new_func(*args, **kwargs):
        print 'arguments: {} {}'.format(args, kwargs)
        return func(*args, **kwargs)
    return new_func

def double_args(func):
    def new_func(*args, **kwargs):
        doubled_args = tuple(a*2 for a in args)
        doubled_kwargs = {k: v*2 for k, v in kwargs.iteritems()}
        return func(*doubled_args, **doubled_kwargs)
    return new_func

def fancy_output(txt='*', n=3):
    def wrap(func):
        def wrapped_func(*args, **kwargs):
            return '{0} {1} {0}'.format(txt*n, func(*args, **kwargs))
        return wrapped_func
    return wrap

def time_dec(func):
    def new_func(*args, **kwargs):
        t1 = time.time()
        ret = func(*args, **kwargs)
        t2 = time.time()
        print t2 - t1, "seconds executing", func.func_name
        return ret
    return new_func


# pie-decorator syntax
# two decorators below equivalent to:
# add_these = double_args(log_args(add_these))
@double_args
@log_args
def add_these(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

@fancy_output('-*-', 2)
def multiply_these(*args):
    return reduce(operator.mul, args)

@time_dec
def snooze(n=3.14):
    print 'sleeping for', n, 'seconds'
    time.sleep(n)


print add_these(9, 13, 11, 9, x=999, z=2112)
print multiply_these(6, 7)
snooze()
