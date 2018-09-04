# Unix shell-style filename matching

import fnmatch
import os


# fnmatch uses case sensitivity of OS
# fnmatchcase always makes case-sensitive comparisons
for f in os.listdir(os.curdir):
    if fnmatch.fnmatch(f, 'O*_qs.py'):
        print f, "matched using fnmatch with pattern 'O*_qs.py'"
    if fnmatch.fnmatchcase(f, 'o*_qs.py'):
        print f, "matched using fnmatchcase with pattern 'o*_qs.py'"


print [f for f in os.listdir(os.curdir) if os.path.isfile(f) and fnmatch.fnmatch(f, 'o*_qs.py')]
