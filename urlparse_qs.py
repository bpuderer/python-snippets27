import urllib
from urlparse import parse_qs, urlparse


# https://tools.ietf.org/html/rfc3986
# http://doriantaylor.com/policy/http-url-path-parameter-syntax

url = "http://user:password@host:80/pathseg1/pathseg2;param1;param2=v1,v2?field1=value1&field2=value2#fragment"
print url

parsed_url = urlparse(url)
print parsed_url

print "scheme:", parsed_url.scheme
print "netloc:", parsed_url.netloc
print "path:", parsed_url.path
print "params:", parsed_url.params
print "query:", parsed_url.query
print "fragment:", parsed_url.fragment
print "username:", parsed_url.username
print "password:", parsed_url.password
print "hostname:", parsed_url.hostname
print "port:", parsed_url.port

qs = parsed_url.query
# & or ; separator
print "parsed query string:", parse_qs(qs)


# build query string
print urllib.urlencode({'foo': 0, 'bar': 1})


# https://www.ietf.org/rfc/rfc1738.txt
p = "/15% off/Lenny&Squiggy"
q = urllib.quote(p)
print q
print urllib.unquote(q)
