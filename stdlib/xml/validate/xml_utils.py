from lxml import etree
from StringIO import StringIO


# http://lxml.de/validation.html
def validate_schema(xsd_str, xml_str):
    xmlschema_doc = etree.parse(StringIO(xsd_str))
    xmlschema = etree.XMLSchema(xmlschema_doc)

    doc = etree.parse(StringIO(xml_str))
    # xmlschema.validate(doc)   returns True/False
    # xmlschema.assertValid(doc)    raises lxml.etree.DocumentInvalid
    xmlschema.assert_(doc)


def validate_schema_from_files(xsd_filename, xml_filename):
    with open(xsd_filename) as f:
        xsd_str = f.read()

    with open(xml_filename) as f:
        xml_str = f.read()

    validate_schema(xsd_str, xml_str)
