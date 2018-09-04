import uuid

# RFC 4122 https://tools.ietf.org/html/rfc4122.html

# version 1 - MAC and date-time
print "Version 1:", uuid.uuid1()

# version 3 - MD5 and namespace
print "Version 3:", uuid.uuid3(uuid.NAMESPACE_DNS, 'github.com')

# version 4 - random
print "Version 4:", uuid.uuid4()

# version 5 - SHA-1 and namespace
print "Version 5:", uuid.uuid5(uuid.NAMESPACE_DNS, 'gitlab.com')
