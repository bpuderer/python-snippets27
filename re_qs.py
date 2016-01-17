r"""
Use raw string notation for regex patterns
to avoid collisions with python special characters

'\' escape character

'.' any char except newline
\d decimal digit, [0-9]
\D non-digit, [^0-9]
\s whitespace, [ \t\n\r\f\v]
\S non-whitespace, [^ \t\n\r\f\v]
\w word, [a-zA-Z0-9_]
\W non-word, [^a-zA-Z0-9_]

\b word boundaries (as defined as any edge between a \w and \W)
\B non-word-boundaries

'*' 0 or more
'+' 1 or more
'?' 0 or 1
'*?', '+?', '??' non greedy versions

'^' start of string
'$' end of string
\A matches only at the start of the string
\Z matches only at the end of the string

'{m}'  exactly m instances
'{m,}' at least m instances
'{m,n}' between m and n (inclusive) instances
'{m,n}?' non-greedy version

[] set of chars, '-' for range, '^' for not, [aeiou], [^aeiou], [a-z]
| or of two regex, A|B
() capture group
"""

import re


text = "Nobody  with a good car needs to be justified"

#match looks for a match at *beginning* of string
result = re.match(r'.*good car', text)
if result:
    print "matched '{}' in '{}' from {} to {} with pattern '{}'".format(result.group(), result.string, result.start(), result.end(), result.re.pattern)

#search looks for first match *anywhere* in string starting at beginning
result = re.search(r'good car', text)
if result:
    print "matched '{}' in '{}' from {} to {} with pattern '{}'".format(result.group(0), result.string, result.start(0), result.end(0), result.re.pattern)

#capture group
result = re.match(r'.*good (\w+)', text)
if result:
    print result.group(1)

#named group
result = re.search(r'good (?P<goodthing>\w+)', text)
if result:
    #returns dictionary of named subgroups of match
    print result.groupdict()
    print result.group('goodthing')
    #can still be referenced by index
    print result.group(1)

#compiling not necessary for scripts with just a few regex
pattern = re.compile(r'good (\w+)')
result = pattern.search(text)
if result:
    print result.group(1)

print re.split(r'\W+', text)
#returned list contains capture group as well
print re.split(r'(\W+)', text)
#can specify max number of splits
print re.split(r'\W+', text, 1)


text = "1abXLIVdefg 2abcdefg 3abczdefg 4abzcdefg 5abdefg 6abczcdefg 7abzczdefg"

#pattern to ensure a single 'c' in between 'b' and 'd'
#using numbers and caps for illustration
#pattern won't make a sub on 'abcdefg' like r'b.*?d' would
print re.sub(r'bd|b[^c].*?d|bc[^d]+?d', 'BCD', text)
#same as sub but returns tuple of string and subs made
print re.subn(r'bd|b[^c].*?d|bc[^d]+?d', 'BCD', text)

#can specify max number of replacements
print re.sub(r'bd|b[^c].*?d|bc[^d]+?d', 'BCD', text, 3)
print re.subn(r'bd|b[^c].*?d|bc[^d]+?d', 'BCD', text, 3)


text = "It's got a cop motor, a 440-cubic-inch plant. It's got cop tires, cop suspension, cop shocks."

#return non-overlapping matches as list
print re.findall(r'cop (\w+)', text)

for m in re.finditer(r'cop \w+', text):
    print m.group(0)


#for matching a string that might have regex metachars
print re.escape(r'.*good \w+')

#clear regex cache
re.purge()
