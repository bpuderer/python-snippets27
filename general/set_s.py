# set - mutable, unordered, contains distinct hashable objects

 
seta = set(["purple", "green", "gold"])
setb = {"black", "gold"}
setc = set(("purple", "green", "black", "gold"))

print "set a:", seta
print "set b:", setb
print "set c:", setc
print

print "a union b:", seta.union(setb)
print "a intersect b:", seta.intersection(setb)
print "a - b:", seta.difference(setb)
print "symmetric difference of a and b:", seta.symmetric_difference(setb)
print "is a subset of b?", seta.issubset(setb)
print "is a subset of c?", seta.issubset(setc)
print "is b superset of c?", setb.issuperset(setc)
print "is c superset of b?", setc.issuperset(setb)

seta.clear()
print "set a after clearing:", seta

seta.add("purple")
seta.add("green")
seta.add("gold")
print "set a after adding purple, green, gold:", seta

setz = seta.copy()
print "set z (shallow copy of set a):", setz

# KeyError raised if element not a member
seta.remove("purple")
print "set a after removing purple:", seta

print "set a after removing an arbitrary element, in this case", seta.pop(), ":", seta

# KeyError *not* raised if element not a member
seta.discard("green")
print "set a after discarding green which may/may not be a member:", seta

print "set z:", setz
