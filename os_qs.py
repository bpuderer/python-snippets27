import fnmatch
import os
import platform
import shlex
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


dirs = [d for d in os.listdir(os.curdir) if os.path.isdir(d)]
print "dirs in current dir:", dirs


# recursively walk directory searching for files
# with Unix filename pattern matching
matches = []
for dirpath, _, filenames in os.walk(os.curdir):
    for filename in fnmatch.filter(filenames, '*.csv'):
        matches.append(os.path.join(dirpath, filename))
print 'csv files from here on down:', matches


print "last modified time:", time.ctime(os.path.getmtime(__file__))
print "ctime:", time.ctime(os.path.getctime(__file__))


#split string using shell-like syntax
#useful with subprocess.Popen args argument
print shlex.split("tail -n20 somefile.log | grep -i spam")
