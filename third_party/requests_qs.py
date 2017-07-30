from uuid import uuid4

import requests


# http://docs.python-requests.org/en/master/api/
# http://docs.python-requests.org/en/master/api/#requests.request
# http://docs.python-requests.org/en/master/api/#requests.Response

# *always* use timeout parameter
# http://docs.python-requests.org/en/master/user/quickstart/#timeouts

# using httpsim.py in python-test repo
requests.delete("http://localhost:1234/books", timeout=0.5)

# POST JSON
book = {'identifier': {'ISBN-10': "0374530874"}, 'title': "The Violent Bear It Away"}
r = requests.post("http://localhost:1234/books", json=book, timeout=0.5)
print r.status_code


print '---'


# GET
r = requests.get('http://localhost:1234/books',
                 params={'qp1': '9', 'qp2': ['28', '3']},
                 headers={'X-Request-ID': str(uuid4())},
                 timeout=0.5)
print r.status_code
# headers dict is case insensitive
print type(r.headers)
print r.headers
print r.headers['content-type']
# can use get to avoid KeyError
print r.headers.get('Content-Type')
print r.encoding
print r.text
print r.json()
