from urlparse import urlparse, parse_qs

url = "http://user:password@host:80/pathseg1/pathseg2?field1=value1&field2=value2#fragment"

print url
parsed_url = urlparse(url)
print "scheme:", parsed_url.scheme
print "netloc:", parsed_url.netloc
print "path:", parsed_url.path
print "query:", parsed_url.query
print "fragment:", parsed_url.fragment
print "username:", parsed_url.username
print "password:", parsed_url.password
print "hostname:", parsed_url.hostname
print "port:", parsed_url.port
print "type of port:", type(parsed_url.port)

qs = parsed_url.query
print "parsed query string:", parse_qs(qs)
