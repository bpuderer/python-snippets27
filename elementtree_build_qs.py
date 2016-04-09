import xml.etree.ElementTree as ET
from xml.dom import minidom


actor_data = [{'name': 'John Cleese', 'birthplace': 'Weston-super-Mare, Somerset, England', 'characters': ['The Black Knight', 'First Centurion', 'Robin Hood', 'Archie Leach']}, {'name': 'Graham Chapman', 'birthplace': 'Leicester, England', 'characters': ['King Arthur', 'Brian']}, {'name': 'Eric Idle', 'birthplace': 'Shields, County Durham, England', 'characters': ['The Dead Collector', 'Harry the Haggler', 'Gunther', 'Berthold']}, {'name': 'Nigel Terry', 'birthplace': 'Bristol, Gloucestershire, England', 'characters': ['King Arthur', 'General Cobb']}, {'name': 'Michael Palin', 'birthplace': 'Broomhill, Sheffield, West Riding of Yorkshire, England', 'characters': ['Sir Galahad', 'Mr. Big Nose', 'Jack Lint', 'Ken Pile']}]

ET.register_namespace('', 'http://people.example.com')
ET.register_namespace('fictional', 'http://characters.example.com')

actors = ET.Element('{http://people.example.com}actors')

for actor in actor_data:
    actor_n = ET.SubElement(actors, 'actor', attrib={'name': actor['name']})
    birthplace_n = ET.SubElement(actor_n, 'birthplace')
    birthplace_n.text = actor['birthplace']
    for character in actor['characters']:
        character_n = ET.SubElement(actor_n, '{http://characters.example.com}character')
        character_n.text = character

#can also set an attribute using set method
#actor_n.set('name', actor['name'])
#or by 
#actor_n.attrib['name'] = actor['name']

xml_str = ET.tostring(actors, encoding='utf-8')
formatted_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
print formatted_xml
