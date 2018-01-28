import sys
import xml.etree.ElementTree as ET

s = sys.stdin.read()
root = ET.fromstring(s)
for i in root.iter():
    print i.tag, i.attrib, i.text
