"""classes demo"""

class MyClass(object):
    """MyClass docstring.  inherit from object = new style object"""

    #class variable. use immutables.
    version = '0.1'

    #watch https://www.youtube.com/watch?v=HTLu2DFOdTg
    #great presentation from Raymond Hettinger
    #docstrings below quote and paraphrase RH
    #if good, useful, correct -> RH
    #if not -> misquote, me

    def __init__(self, val):
        """dunder (double underscore) init is *not* a constructor.

        self is the instance that has already been made when init is called.
        it is an initializer that populates self"""
        self.lst = []
        self.val = val
        print self.__no_clash()    #demo prevention of name clash

    def add(self, x):
        """add x to lst"""
        self.lst.append(x)

    def double_add(self, x):
        """add x twice"""
        self.add(x)
        self.add(x)

    @staticmethod
    def func_in_class():
        """purpose of static method is to attach functions to classes

        because that's where people look for it"""
        return "just a function hanging out in a class"

    def no_clash(self):
        """demo name mangling

        name mangling used to prevent name clashes with subclassing.
        """
        return self.val * 1.0

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

    __no_clash = no_clash


class MyClass2(MyClass):
    """MyClass2 docstring"""

    def double_add(self, x):
        """override method. add two times x to lst, not x twice"""
        self.add(x*2)

    def no_clash(self):
        """override no_clash. demo name mangling.  return 110% of val"""
        return self.val * 1.1


a = MyClass(42)
print a.no_clash()
print a.func_in_class()
a.add(2112)
a.double_add(2010)
print a

print '--'

#b uses alt constructor
b = MyClass.fromtripleval(27)
print b.no_clash()
print b.func_in_class()
b.add(2112)
b.double_add(2010)
print b

print '--'

#c is a MyClass2 not MyClass
c = MyClass2(10)
print c.no_clash()
print c.func_in_class()
c.add(2001)
c.double_add(2010)
print c

print '--'

print a + b
print b + c
