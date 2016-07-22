class MyClass(object):
    """MyClass docstring"""

    #class variable. immutable.
    i = 123

    #https://docs.python.org/2.7/tutorial/classes.html#private-variables-and-class-local-references
    #convention to denote private / implementation detail:
    #start name with an underscore

    #use name mangling to prevent name clashes when subclassing
    #https://www.youtube.com/watch?v=HTLu2DFOdTg&t=33m25s
    #RH- "one of my problems with a variable named self is it implies that it's you.
    #but it's not you.  it is you or your children."
    #RH- "making sure that self actually refers to you"
    #RH- "...all about freedom.  It makes your subclasses free to override any one method
    #without breaking the others."

    def __init__(self, val):
        self.lst = []
        self.val = val
        print self.__no_clash()

    def add(self, x):
        self.lst.append(x)

    def double_add(self, x):
        self.add(x)
        self.add(x)

    def no_clash(self):
        return 'no_clash from MyClass'

    def __str__(self):
        return "val:"+str(self.val)+" lst:"+str(self.lst)+" i:"+str(self.i)

    def __add__(self, other):
        tmp = MyClass(self.val + other.val)
        tmp.lst = self.lst + other.lst
        return tmp

    __no_clash = no_clash


class MyClass2(MyClass):
    def double_add(self, x):
        self.add(x*2)

    def no_clash(self):
        return 'no_clash from MyClass2'


a = MyClass(42)
print a.no_clash()
a.add(2112)
a.double_add(2010)
print a

print '--'

b = MyClass2(10)
print b.no_clash()
b.add(2001)
b.double_add(2010)
print b

print '--'

print a + b
