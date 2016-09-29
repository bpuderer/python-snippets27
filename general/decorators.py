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

# pie-decorator syntax
@double_args
@log_args
def add_these(*args, **kwargs):
    return sum(args) + sum(kwargs.values())


print add_these(9, 13, 11, 9, x=999, z=2112)
