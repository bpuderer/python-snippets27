# https://www.python.org/dev/peps/pep-0227/

# http://effbot.org/zone/closure.htm
# Fredrik Lundh
# "a function that can refer to environments that are no longer active (such as
# the local namespace of an outer function, even after that function has returned)"


# http://www.shutupandship.com/2012/01/python-closures-explained.html
# Praveen Gollakota
def generate_power_func(n):
    def nth_power(x):
        return x**n
    return nth_power

raised_to_5th = generate_power_func(5)
print raised_to_5th.__closure__
print raised_to_5th.__closure__[0]
print raised_to_5th.__closure__[0].cell_contents
print raised_to_5th(2)


print '---'


# http://stackoverflow.com/a/141426
# J.F. Sebastian
# http://stackoverflow.com/users/4279/j-f-sebastian
def make_counter():
    #i = 0
    i = [0]
    def counter():
        #i += 1    -> UnboundLocalError
        #see PEP 3104 and nonlocal keyword implemented in python 3
        #using a mutable object as a workaround
        i[0] += 1
        return i[0]
    return counter

c = make_counter()
print c.__closure__[0].cell_contents
print c()
print c.__closure__[0].cell_contents
print c()
