import xml.etree.ElementTree as ET
#enhanced example based on Python Software Foundation xml.etree.ElementTree doc
#https://docs.python.org/2/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
#https://docs.python.org/2/library/xml.etree.elementtree.html#xpath-support

ns = {'real_person': 'http://people.example.com',
      'role': 'http://characters.example.com'}

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
            <birthplace>Santa Barbara, California, U.S.</birthplace>
            <fictional:character>King Arthur</fictional:character>
        </artist>
    </extras>
</actors>
"""

#parse from file
#tree = ET.parse('test.xml')
#root = tree.getroot()

root = ET.fromstring(xml_text)

print "root.tag:", root.tag
print "root.attrib:", root.attrib

print "\nChild elements of root:"
for child in root:
    print child.tag, child.attrib, child.text

print "\nroot[0][2] text:", root[0][2].text

print "\nIterate entire tree:"
for i in root.iter():
    print i.tag, i.attrib, i.text

print "\nList the birthplace of each actor:"
for birthplace in root.iterfind('real_person:actor/real_person:birthplace', ns):
    print birthplace.text

print "\nWalk tree:"
for actor in root.findall('real_person:actor', ns):
    #print actor.attrib['name'], "of", actor.find('real_person:birthplace', ns).text
    #get and findtext support returning a default value if not found
    #if a default is not set for findtext and a namespace is required,
    #use the named argument 'namespaces'  Ex. namespaces=ns
    #this appears to be missing from the 2.7 documentation but is present in 3.3+
    print actor.get('name', 'Default Name'), "of", actor.findtext('real_person:birthplace', 'Default Place', ns)
    for char in actor.findall('role:character', ns):
        print ' |-->', char.text

print "\nWhich character(s) did Eric Idle play?"
for result in root.findall("./real_person:actor[@name='Eric Idle']/role:character", ns):
    #printing tag is helpful when debugging xpath
    print result.text

print "\nWhich actor(s) played Robin Hood?"
for result in root.findall("./real_person:actor[role:character='Robin Hood']", ns):
    #print result.attrib['name']
    #get can return a default value if attribute not found
    print result.get('name')

print "\nWhich actor(s) played King Arthur?"
for result in root.findall("./real_person:actor[role:character='King Arthur']", ns):
    print result.attrib['name']

print "\nWhere are the actor(s) from who played King Arthur?"
for result in root.findall("./real_person:actor[role:character='King Arthur']/real_person:birthplace", ns):
    print result.text

print "\nLast role listed for each actor:"
for result in root.findall("./real_person:actor/role:character[last()]", ns):
    print result.text

# selects all birthplace elements anywhere in tree
print "\nAll birthplaces:"
for result in root.findall(".//real_person:birthplace", ns):
    print result.text

# selects all elements that have a character subelement set to King Arthur
print "\nWho played King Arthur?"
for result in root.findall(".//*[role:character='King Arthur']", ns):
    print result.attrib['name']
