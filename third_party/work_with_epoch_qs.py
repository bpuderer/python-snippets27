import time
import calendar
from datetime import datetime
import pytz
from dateutil.parser import parse


# datetime -> epoch

# naive

now = datetime.now()
print time.mktime(now.timetuple())

utc_now = datetime.utcnow()
print calendar.timegm(utc_now.utctimetuple())

# aware

utc = pytz.UTC
eastern = pytz.timezone('US/Eastern')

now_eastern = datetime.now(eastern)
now_utc = datetime.now(utc)

print calendar.timegm(now_eastern.utctimetuple())
print calendar.timegm(now_utc.utctimetuple())


dt = parse("2016-03-19T17:10:00-04:00")
print calendar.timegm(dt.utctimetuple())



# epoch -> datetime

# naive

print datetime.fromtimestamp(time.time())
print datetime.utcfromtimestamp(time.time())

# aware

print datetime.fromtimestamp(time.time(), utc)
print datetime.fromtimestamp(time.time(), eastern)
