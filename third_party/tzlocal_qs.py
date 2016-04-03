from datetime import datetime
import pytz
from tzlocal import get_localzone


# tzlocal returns a pytz timezone for the local timezone
# https://github.com/regebro/tzlocal
tz = get_localzone()
print type(tz)
print tz

print "Current local time:\t\t", datetime.now(tz).isoformat()

# use pytz localize() to localize a naive datetime
local_dt = tz.localize(datetime(year=1991, month=8, day=25, hour=16, minute=57, second=8))
print "Local time:\t\t\t", local_dt.isoformat()

# can convert using standard astimezone()
utc_dt = local_dt.astimezone(pytz.utc)
print "Converted to UTC time:\t\t", utc_dt.isoformat()

pac_dt = utc_dt.astimezone(pytz.timezone('US/Pacific'))
print "Converted to Pacific time:\t", pac_dt.isoformat()
