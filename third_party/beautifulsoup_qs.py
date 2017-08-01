from bs4 import BeautifulSoup
# import urllib2
# import requests


# response = urllib2.urlopen('http://python.org/')
# html_doc = response.read()

# r = requests.get('http://python.org/')
# html_doc = r.text

html_doc = """
<!DOCTYPE html>
<html>
<head>
<title>The Title</title>
</head>
<body>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Python_(programming_language)" id="link1">Python (programming language)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Monty_Python" id="link2">Monty Python</a></li>
</ul>
</body>
</html>
"""

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# html.parser is default but if not specified, UserWarning
soup = BeautifulSoup(html_doc, 'html.parser')
print soup.a
print soup.a.attrs
print soup.a['href']
print soup.a.string

print '---'

# find_all can take string, regex, list, True, function
for a in soup.find_all('a'):
    # single string within tag
    print a.string
    # get all child strings
    print a.text
    # can avoid KeyError
    print a.get('href')
    print a.has_attr('spam')
    print '---'

print soup.find('a', attrs={'href': "https://en.wikipedia.org/wiki/Monty_Python"})
print soup.find('a', string="Monty Python")
print soup.find(id="link2")

print '---'

# .children returns generator, .contents returns list. both return direct children
# .descendants returns generator. recursive
print list(soup.ul.children)
print '-'
print soup.ul.contents
print '-'
print list(soup.ul.descendants)
