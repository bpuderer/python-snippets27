from StringIO import StringIO


# class StringIO.StringIO([buffer])
# aka "memory files"
f = StringIO()
f.write("first line\n")
f.writelines(["second line\n", "third line\n"])
print "whole file's contents:\n", f.getvalue()

print "current position:", f.tell()
print "setting position back to 0..."
f.seek(0)
print "first 4 bytes:", f.read(4)
print "until EOL or EOF:", f.readline()
print "until EOF:\n", f.read()

print "setting position back to 0..."
f.seek(0)
print "list of lines:", f.readlines()
f.close()


print "---"


# position=0 regardless if initialized with string
f = StringIO("This parrot is no more. It has ceased to be.")
print "initial position:", f.tell()
print "contents:", f.getvalue()
f.truncate(23)
print "contents after truncating at 23:", f.getvalue()
f.close()
