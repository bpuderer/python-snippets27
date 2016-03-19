import datetime
import pytz
import time


# work in utc and only convert to localtime when
# generating output for humans.
# https://www.youtube.com/watch?v=LnVkLXRIbIg#t=13m09s

utc = pytz.UTC
eastern = pytz.timezone('US/Eastern')


# UTC aware datetime
# DONT use timezones with daylight savings time
# with the tzinfo argument of the datetime constructor.
print datetime.datetime(1991, 8, 25, 20, 57, 8, tzinfo=utc)

# UTC aware datetime from POSIX timestamp
print datetime.datetime.fromtimestamp(time.time(), utc)


# create an aware datetime in a given timezone from wall time.
# localize also has an is_dst parameter to handle ambiguous
# timestamps during DST transitions.
# if not passed or set to False, ambiguous timestamps are set
# to STD.  is_dst=True, DST.
# if is_dst=None, pytz.tzinfo.AmbiguousTimeError is raised
print eastern.localize(datetime.datetime(1991, 8, 25, 16, 57, 8))


# create an aware datetime for this instant in a given timezone
now_eastern = datetime.datetime.now(eastern)
print now_eastern.isoformat()

now_utc = datetime.datetime.now(utc)
print now_utc.isoformat()


# convert aware datetime to a different tz
# see note at top
print now_utc.astimezone(eastern)
