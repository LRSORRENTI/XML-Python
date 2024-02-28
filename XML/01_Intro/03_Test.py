import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('02_Student.xml')
root = tree.getroot()

# Update the hour to 10
hour_element = root.find('hour')
if hour_element is not None:
    hour_element.text = '10'

# Change Martha to Martin
for student in root.findall('student'):
    firstname_element = student.find('firstname')
    if firstname_element is not None and firstname_element.text.strip() == 'Martha':
        firstname_element.text = 'Martin'

# Write the updated XML back to the file
tree.write('updated_xml_file.xml')
