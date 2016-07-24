# -*- coding: utf-8 -*-

#must watch/read:
#https://www.youtube.com/watch?v=sgHbC6udIqc
#http://nedbatchelder.com/text/unipain.html

#https://docs.python.org/2/library/codecs.html#standard-encodings
#http://unicode.org/charts/

#unicode- code points
#code point- number for each character 0-10FFFF
#normally referred to by "U+" followed by number
#Hi ℙƴ☂ℌøἤ
my_unicode = u'Hi \u2119\u01b4\u2602\u210c\xf8\u1f24'
print my_unicode, "type:", type(my_unicode), "length:", len(my_unicode)
print repr(my_unicode)
print '--'

#str- sequence of bytes
#encode- code points -> bytes
my_utf8 = my_unicode.encode('utf-8')
print my_utf8, "type:", type(my_utf8), "length:", len(my_utf8)
print repr(my_utf8)

print '--'

#decode- bytes -> code points
back = my_utf8.decode('utf-8')
print back, "type:", type(back), "length:", len(back)
print repr(back)

print '---'

#U+00A2 = ¢
my_unicode = u'95\u00a2'
print repr(my_unicode)
print my_unicode
#¢ not valid in ascii
#2nd arg is 'errors'.  possible values:
#strict(default), ignore, replace, xmlcharrefreplace, backslashreplace
#would have raised UnicodeEncodeError
my_ascii = my_unicode.encode('ascii', 'replace')
print type(my_ascii), my_ascii

print '---'

#for testing
#₩ℌ∀☂, ♏∃ ℱα☤Ḻ⁇
uni_test = u'\u20a9\u210c\u2200\u2602, \u264f\u2203 \u2131\u03b1\u2624\u1e3a\u2047'
print uni_test
