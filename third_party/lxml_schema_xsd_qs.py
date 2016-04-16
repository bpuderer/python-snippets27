from lxml import etree
from StringIO import StringIO


# http://lxml.de/validation.html
xmlschema_txt = """<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
   <xs:element name="actors">
      <xs:complexType>
         <xs:sequence>
            <xs:element name="actor" maxOccurs="unbounded">
               <xs:complexType>
                  <xs:sequence>
                     <xs:element name="birthplace" type="xs:string" />
                     <xs:element name="character" type="xs:string" maxOccurs="unbounded" />
                  </xs:sequence>
                  <xs:attribute name="name" type="xs:string" use="required" />
               </xs:complexType>
            </xs:element>
         </xs:sequence>
      </xs:complexType>
   </xs:element>
</xs:schema>
"""

valid_xml_text = """<?xml version="1.0"?>
<actors>
    <actor name="John Cleese">
        <birthplace>Weston-super-Mare, Somerset, England</birthplace>
        <character>Black Knight</character>
        <character>First Centurion</character>
        <character>Robin Hood</character>
        <character>Archie Leach</character>
    </actor>
    <actor name="Graham Chapman">
        <birthplace>Leicester, England</birthplace>
        <character>King Arthur</character>
        <character>Brian</character>
    </actor>
    <actor name="Eric Idle">
        <birthplace>South Shields, County Durham, England</birthplace>
        <character>The Dead Collector</character>
        <character>Harry the Haggler</character>
        <character>Gunther</character>
        <character>Berthold</character>
    </actor>
    <actor name="Nigel Terry">
        <birthplace>Bristol, Gloucestershire, England</birthplace>
        <character>King Arthur</character>
        <character>General Cobb</character>
    </actor>
    <actor name="Michael Palin">
        <birthplace>Broomhill, Sheffield, West Riding of Yorkshire, England</birthplace>
        <character>Sir Galahad</character>
        <character>Mr. Big Nose</character>
        <character>Jack Lint</character>
        <character>Ken Pile</character>
    </actor>
</actors>
"""

invalid_xml_text = """<?xml version="1.0"?>
<actors>
    <actor name="John Cleese">
        <character>Black Knight</character>
        <character>First Centurion</character>
        <character>Robin Hood</character>
        <character>Archie Leach</character>
        <birthplace>Weston-super-Mare, Somerset, England</birthplace>
    </actor>
</actors>
"""


xmlschema_doc = etree.parse(StringIO(xmlschema_txt))
xmlschema = etree.XMLSchema(xmlschema_doc)


valid_xml_doc = etree.parse(StringIO(valid_xml_text))
invalid_xml_doc = etree.parse(StringIO(invalid_xml_text))


# returns True if doc conforms to schema, False if not
print "Conforms to schema:", xmlschema.validate(valid_xml_doc)

# lxml.etree.DocumentInvalid raised on failure
xmlschema.assertValid(valid_xml_doc)

# AssertionError raised on failure
xmlschema.assert_(valid_xml_doc)


print "Conforms to schema:", xmlschema.validate(invalid_xml_doc)
#xmlschema.assertValid(invalid_xml_doc)
xmlschema.assert_(invalid_xml_doc)
