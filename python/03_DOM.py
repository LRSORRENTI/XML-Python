# In this code, we use the DOM approach
# to parse the XML file and extract the information
# about each person. This method is more
# straightforward for this particular use case,
# as the XML structure is simple and the file size 
# is not large. However, for larger XML files or 
# more complex processing requirements, 
# the SAX approach might be more suitable.

# This method uses the xml.dom.minidom module
# to parse the XML file, which is a different
# approach compared to the xml.sax method used
# in 02_Class.py. Here's a comparison:

# Comparison:
# DOM (xml.dom.minidom):

# Pros:

# - Simpler and more intuitive for small to medium-sized
# XML files.
# - Easier to navigate and manipulate the XML tree 
# structure.

# Cons:

# - Less memory-efficient for large XML files, 
# as it loads the entire document into memory.
# - Can be slower than SAX for processing large files.

# SAX (xml.sax):

# Pros:
# - More memory-efficient for large XML files, 
# as it uses a stream-based approach.
# - Potentially faster for processing large files.

# Cons:
# - More complex to implement, especially for
# complex XML structures.
# - Less convenient for manipulating the XML 
# tree structure.

# Importing the minidom module from the xml.dom package
import xml.dom.minidom

# Parsing the XML file and getting the document element (root)
domtree = xml.dom.minidom.parse('XML/people.xml')
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
