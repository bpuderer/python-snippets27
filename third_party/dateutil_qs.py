from dateutil.parser import parse


dt = parse("1991-08-25 16:57:08-04:00")
print dt.isoformat()
print type(dt)

print parse("2016-03-19T18:58:47.318285+00:00").isoformat()
print parse("Sat Mar 19 3:34 PM").isoformat()
print parse("March 19, 2016 3:34 PM EDT").isoformat()
print parse("20160311T034540Z").isoformat()
print parse("05/03/2016", dayfirst=True).isoformat()
print parse("27 September 1983").isoformat()
