import time


print "snoozing 300 ms...zzzzzzz"
time.sleep(0.3)

# precision is platform dependent but a float is always returned
print "seconds since epoch as a float:", time.time()

# returns string for a tuple/struct_time in format "%a %b %d %H:%M:%S %Y"
# if no arg is provided it uses localtime()
print "current local time string:", time.asctime()
print "when is epoch?", time.asctime(time.gmtime(0))

# seconds since epoch to local string
# if no arg provided it uses time()
print "current local time string:", time.ctime()
print "10 minutes ago from current local time string:", time.ctime(time.time()-600)

# seconds since epoch to struct_time in UTC
# if no arg is provided is uses time()
print "current UTC time as struct_time", time.gmtime()
# same as gmtime() except local
print "local time as struct_time", time.localtime()

# reverse of localtime() and arg is required
print "sec since epoch from a *local* struct_time", time.mktime(time.localtime())

# struct_time to string with format string
# defaults to localtime() if t arg not provided
print "local time with format string", time.strftime("%a, %B %d, %Y %I:%M:%S %p")
# no %f for microseconds as in datetime
print "UTC time with format string", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

# string to struct_time
# defaults to format from ctime() if string arg not provided: "%a %b %d %H:%M:%S %Y"
print "local struct_time from string", time.strptime(time.ctime())
print "struct_time from string", time.strptime("31/10/2016 07:30:00 PM", "%d/%m/%Y %I:%M:%S %p")
