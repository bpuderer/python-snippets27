import json
import xmltodict


simple_xml = """<?xml version="1.0" encoding="UTF-8"?>
<library name="Algiers Regional Library">
   <books>
      <book format="hardcover">
         <title>Wise Blood</title>
         <author>Flannery O'Connor</author>
      </book>
      <book format="paperback">
         <title>The Moviegoer</title>
         <author>Walker Percy</author>
      </book>
   </books>
</library>"""

library = xmltodict.parse(simple_xml)
print json.dumps(library, indent=4)

print "Library name:", library['library']['@name']
print "Titles:"
for book in library['library']['books']['book']:
    print book['title']
print '----'


xml_with_ns = """<?xml version="1.0" encoding="UTF-8"?>
<actors xmlns="http://people.example.com" xmlns:fictional="http://characters.example.com">
   <actor name="John Cleese">
      <birthplace>Weston-super-Mare, Somerset, England</birthplace>
      <fictional:character>Black Knight</fictional:character>
      <fictional:character>First Centurion</fictional:character>
      <fictional:character>Robin Hood</fictional:character>
      <fictional:character>Archie Leach</fictional:character>
   </actor>
   <actor name="Eric Idle">
      <birthplace>South Shields, County Durham, England</birthplace>
      <fictional:character>The Dead Collector</fictional:character>
      <fictional:character>Harry the Haggler</fictional:character>
      <fictional:character>Gunther</fictional:character>
      <fictional:character>Berthold</fictional:character>
   </actor>
   <actor name="Michael Palin">
      <birthplace>Broomhill, Sheffield, West Riding of Yorkshire, England</birthplace>
      <fictional:character>Sir Galahad</fictional:character>
      <fictional:character>Mr. Big Nose</fictional:character>
      <fictional:character>Jack Lint</fictional:character>
      <fictional:character>Ken Pile</fictional:character>
   </actor>
</actors>"""


# process_namespaces=False by default, ns defs are just attribs
# optional namespaces arg allows shorthand defs and None is treated as the default ns
# NOTE: namespace dict reverses keys and values as seen in ElementTree Element.findall()
ns = {'http://people.example.com': None, 'http://characters.example.com': 'role'}
actors_ns = xmltodict.parse(xml_with_ns, process_namespaces=True, namespaces=ns)
print json.dumps(actors_ns, indent=4)

for actor in actors_ns['actors']['actor']:
    print 'Actor:', actor['@name'],
    print '\tRoles:', 
    for role in actor['role:character']:
    #for role in actor[ns['http://characters.example.com']+':character']:
        print role,
    print
