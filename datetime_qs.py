from datetime import datetime, date, time, timedelta
import time as time_module
import calendar


# class datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])
print "datetime:"

# current local datetime
print datetime.today()

# current local datetime with. tz optional
print datetime.now()

# current UTC datetime
print datetime.utcnow()

# local datetime from POSIX timestamp. optional tz
print datetime.fromtimestamp(time_module.time())

# UTC datetime from POSIX timestamp
print datetime.utcfromtimestamp(time_module.time())

utc_now = datetime.utcnow()
# defaults to 'T' character between date and time
print "ISO8601 format:", utc_now.isoformat()
print utc_now.isoformat(' ')

# format string representation
print utc_now.strftime("%a, %B %d, %Y %I:%M:%S %p")

print utc_now.year, utc_now.month, utc_now.day, utc_now.hour, utc_now.minute, utc_now.second, utc_now.microsecond
print utc_now.date()
print utc_now.time()
print calendar.day_name[utc_now.weekday()]
print calendar.month_name[utc_now.month]

# build a datetime from a date and time
print datetime.combine(date.today(), time(7, 30))

# local datetime but in 1985
print datetime.now().replace(year=1985)



# class datetime.date(year, month, day)
print "---\ndate:"

some_date = date(1994, 4, 5)
print some_date

# current local date
today = date.today()
print today.isoformat()
print today.day, today.month, today.year

# local date from POSIX timestamp
from_ts = date.fromtimestamp(time_module.time())
print from_ts.strftime("%A, %B %d, %Y")



# class datetime.time([hour[, minute[, second[, microsecond[, tzinfo]]]]])
print "---\ntime:"

lunch_time = time(12, 15, 0)
print lunch_time.isoformat()
print lunch_time.strftime("%H|%M|%S.%f")



# timedelta - difference between date, time or datetime instances
# datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
# can only access days, seconds, microseconds
print "---\ntimedelta:"

td = timedelta(days=2, hours=3)
print td.total_seconds()

print "1 hr, 27 min, 32 sec from now:", datetime.now() + timedelta(hours=1, minutes=27, seconds=32)

print "since Usenet post:", datetime.utcnow() - datetime(year=1991, month=8, day=25, hour=20, minute=57, second=8)

print "days from Jan 1:", date.today() - date.today().replace(month=1, day=1)



# create datetime from string
print "---\nstrptime():"

dt = datetime.strptime("31/10/2016 07:30:00 PM", "%d/%m/%Y %I:%M:%S %p")
print dt.isoformat()

