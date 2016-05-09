import fnmatch
import os
import platform
import socket
import time


print os.name, platform.system(), platform.release()


print "pid:", os.getpid()


print "hostname:", socket.gethostname()
print "fqdn:", socket.getfqdn()


os.environ['PYTEST'] = 'set from py script'
# getenv returns None if env variable does not exist
# or an optional default
print os.getenv('PYTEST', 'default val')


# recursively walk directory searching for files
# with Unix filename pattern matching
matches = []
for root, dirnames, filenames in os.walk('.'):
    for filename in fnmatch.filter(filenames, '*.csv'):
        matches.append(os.path.join(root, filename))
print 'csv files from here on down:', matches


print "last modified time:", time.ctime(os.path.getmtime(__file__))
print "ctime:", time.ctime(os.path.getctime(__file__))
