import glob

# find pathnames matching Unix shell style pattern

print glob.glob("o*.py")

# iglob returns iterator
for pathname in glob.iglob("o*.py"):
    print pathname
