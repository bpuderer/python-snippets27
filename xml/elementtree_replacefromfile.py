import xml.etree.ElementTree as ET


# https://docs.python.org/2/library/xml.etree.elementtree.html

tree = ET.parse("test.xml")
root = tree.getroot()

print "ORIGINAL:", ET.tostring(root, encoding='utf-8')

b = root.find('b')
b.text = "update!"
b.attrib['id'] = "321"

print "UPDATED:", ET.tostring(root, encoding='utf-8')

#print "tree's type:", type(tree)
#print "root's type:", type(root)
#tree.write('updated.xml')
