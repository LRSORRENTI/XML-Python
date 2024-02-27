# Importing the minidom module from the xml.dom package
import xml.dom.minidom

# Parsing the XML file 'people2.xml' and getting the document element (root)
domtree = xml.dom.minidom.parse('XML/people2.xml')
group = domtree.documentElement

# Getting all the 'person' elements from the document
people = group.getElementsByTagName('person')

# Iterating through each 'person' element
for person in people:
    # Printing the ID attribute of the person
    print(f"-- Person {person.getAttribute('id')} --")
    
    # Extracting and printing the details of each person
    name = person.getElementsByTagName('name')[0].childNodes[0].nodeValue
    age = person.getElementsByTagName('age')[0].childNodes[0].nodeValue
    weight = person.getElementsByTagName('weight')[0].childNodes[0].nodeValue
    height = person.getElementsByTagName('height')[0].childNodes[0].nodeValue
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Weight: {weight}")
    print(f"Height: {height}")

# Modifying the 'name' value of the first person in the list
people[0].getElementsByTagName('name')[0].childNodes[0].nodeValue = "Alex Warm"

# Setting a new ID attribute value for the first person
people[0].setAttribute("id", "200")

# Adding a new attribute 'newattr' with the value "Hello world" to the first person
people[0].setAttribute("newattr", "Hello world")

# Writing the modified XML document back to the file 'people2.xml'
domtree.writexml(open('XML/people2.xml', 'w'))

# In this code, after extracting and printing the 
# details of each person in the XML file, we modify 
# the 'name' value of the first person, set a new ID 
# attribute for the first person, and add a new 
# attribute 'newattr' to the first person. Finally, 
# we write the modified XML document back to the file 
# 'people2.xml'.

# As you can see bwloe Jennifer Cold is now Alex Warm
# <?xml version="1.0" ?><group>
#     <person id="200" newattr="Hello world">
#         <name>Alex Warm</name>
#         <age>20</age>
#         <weight>80</weight>
#         <height>180</height>
#     </person>
#     <person id="2">
#         <name>Mike Davis</name>
#         <age>45</age>
#         <weight>82</weight>
#         <height>185</height>
#     </person>
#     <person id="3">
#         <name>Anna Johnson</name>
#         <age>33</age>
#         <weight>67</weight>
#         <height>167</height>
#     </person>
# </group>