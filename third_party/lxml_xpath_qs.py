from lxml import etree
from StringIO import StringIO


# lxml provides full XPath syntax unlike ElementTree's ElementPath
# https://www.w3.org/TR/xpath/
# http://lxml.de/xpathxslt.html
# http://lxml.de/api/lxml.etree._ElementTree-class.html#xpath
# http://www.ibm.com/developerworks/library/x-hiperfparse/
# http://infohost.nmt.edu/tcc/help/pubs/pylxml/web/xpath.html
# https://docs.python.org/2/library/xml.etree.elementtree.html#supported-xpath-syntax


simple = '<foo><bar attr1="attrval1_1" attr2="attrval1_2">barval1</bar>first bar tail<bar attr2="attrval2_2">barval2</bar></foo>'
#tree = etree.fromstring(simple)
tree = etree.parse(StringIO(simple))

for r in tree.xpath('/foo/bar'):
    print "tag:", r.tag
    print "attrib:", r.attrib
    print "text:", r.text
    print "tail:", r.tail
    print "-"


print "----"


xml_text = """<?xml version="1.0"?>
<actors xmlns:fictional="http://characters.example.com"
        xmlns="http://people.example.com">
    <actor name="John Cleese">
        <birthplace>Weston-super-Mare, Somerset, England</birthplace>
        <fictional:character>Black Knight</fictional:character>
        <fictional:character>First Centurion</fictional:character>
        <fictional:character>Robin Hood</fictional:character>
        <fictional:character>Archie Leach</fictional:character>
    </actor>
    <actor name="Graham Chapman">
        <birthplace>Leicester, England</birthplace>
        <fictional:character>King Arthur</fictional:character>
        <fictional:character>Brian</fictional:character>
    </actor>
    <actor name="Eric Idle">
        <birthplace>South Shields, County Durham, England</birthplace>
        <fictional:character>The Dead Collector</fictional:character>
        <fictional:character>Harry the Haggler</fictional:character>
        <fictional:character>Gunther</fictional:character>
        <fictional:character>Berthold</fictional:character>
    </actor>
    <actor name="Nigel Terry">
        <birthplace>Bristol, Gloucestershire, England</birthplace>
        <fictional:character>King Arthur</fictional:character>
        <fictional:character>General Cobb</fictional:character>
    </actor>
    <actor name="Michael Palin">
        <birthplace>Broomhill, Sheffield, West Riding of Yorkshire, England</birthplace>
        <fictional:character>Sir Galahad</fictional:character>
        <fictional:character>Mr. Big Nose</fictional:character>
        <fictional:character>Jack Lint</fictional:character>
        <fictional:character>Ken Pile</fictional:character>
    </actor>
    <extras>
        <artist name="Mel Ferrer">
            <birthplace>Elberon, New Jersey, U.S.</birthplace>
            <fictional:character>King Arthur</fictional:character>
        </artist>
    </extras>
</actors>
"""

tree = etree.parse(StringIO(xml_text))
ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

print "Birthplaces:", tree.xpath('//real_person:birthplace/text()', namespaces=ns)

print "Actor names:", tree.xpath('//real_person:actor/@name', namespaces=ns)

print "Characters:", tree.xpath('//role:character/text()', namespaces=ns)

# float is always returned if XPath result is numeric
print "Actor count:", int(tree.xpath('count(//real_person:actor)', namespaces=ns))

print "Character Jack Lint found:", tree.xpath("boolean(//role:character[text()='Jack Lint'])", namespaces=ns)

# can make a callable function from an XPath expression
# better performance when evaluating the same XPath over and over
michael_palin_found = etree.XPath("boolean(//real_person:actor[@name='Michael Palin'])", namespaces=ns)
print "Actor Michael Palin found:", michael_palin_found(tree)
