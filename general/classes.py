"""class demo

highly recommend watching https://www.youtube.com/watch?v=HTLu2DFOdTg
great presentation from python core dev Raymond Hettinger
most docstrings below quote and paraphrase RH
"""

class MyClass(object):
    """MyClass docstring.  inherit from object = new style object"""

    #class variable. use immutables.
    version = '0.1'

    def __init__(self, val):
        """dunder (double underscore) init is *not* a constructor.

        self is the instance that has already been made when init is called.
        it is an initializer that populates self
        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=7m40s"""
        self.lst = []
        self.val = val

    def add(self, x):
        """add x to lst"""
        self.lst.append(x)

    def double_add(self, x):
        """add x twice"""
        self.add(x)
        self.add(x)

    def foo(self):
        """foo returns double bar"""
        return self.__bar() * 2

    def bar(self):
        """bar returns 100% of val
        
        name mangling used to prevent name clashes with subclassing
        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=33m25s"""
        return self.val * 1.0

    @staticmethod
    def func_in_class():
        """purpose of static method is to attach functions to classes

        why? because that's where people look for it
        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=30m8s"""
        return "just a function hanging out in a class"

    @classmethod
    def fromtripleval(cls, tval):
        """alternative constructor

        https://www.youtube.com/watch?v=HTLu2DFOdTg&t=23m28s"""
        val = tval / 3
        return cls(val)

    def __str__(self):
        return "val:"+str(self.val)+" lst:"+str(self.lst)+" ver:"+self.version

    def __add__(self, other):
        tmp = MyClass(self.val + other.val)
        tmp.lst = self.lst + other.lst
        return tmp

    __bar = bar


class MyClass2(MyClass):
    """MyClass2 inherits from MyClass"""

    def double_add(self, x):
        """add two times x to lst, not x twice"""
        self.add(x*2)

    def bar(self):
        """demo name mangling. return 110% of val"""
        return MyClass.bar(self) * 1.1
        

a = MyClass(42)
print a.func_in_class()
print a.foo(), a.bar()
a.add(2112)
a.double_add(2010)
print a

print '--'

#b uses alt constructor
b = MyClass.fromtripleval(27)
print b

print '--'

#c is a MyClass2
c = MyClass2(10)
#foo uses MyClass bar, not MyClass2
print c.foo(), c.bar()
c.add(2001)
c.double_add(2010)
print c

print '--'

print a + b
print a + c
