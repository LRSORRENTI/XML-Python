# Importing the necessary modules from the xml.sax package
import xml.sax
from xml.sax.xmlreader import AttributesImpl

# Defining a custom handler class that inherits from xml.sax.ContentHandler
class PeopleHandler(xml.sax.ContentHandler):
    
    # Method called at the start of an XML element
    def startElement(self, name: str, attrs: AttributesImpl) -> None:
        self.current = name  # Storing the name of the current element
        if name == "person":
            # Printing the ID attribute of the person element
            print(f"-- Person {attrs['id']} --")
    
    # Method called for the character data within XML elements
    def characters(self, content: str) -> None:
        # Storing the content based on the current element name
        if self.current == "name":
            self.name = content
        elif self.current == "age":
            self.age = content
        elif self.current == "weight":
            self.weight = content
        elif self.current == "height":
            self.height = content
    
    # Method called at the end of an XML element
    def endElement(self, name: str) -> None:
        # Printing the stored content when the end of an element is reached
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print(f"Age: {self.age}")
        elif self.current == "weight":
            print(f"Weight: {self.weight}")
        elif self.current == "height":
            print(f"Height: {self.height}")
        self.current = ""  # Resetting the current element name

# Creating an instance of the custom handler class
handler = PeopleHandler()
# Creating an XML parser
parser = xml.sax.make_parser()
# Setting the content handler for the parser to the custom handler
parser.setContentHandler(handler)
# Parsing the XML file
parser.parse('XML/people.xml')


# -- Person 1 --
# Name: Jennifer Cold
# Age: 20
# Weight: 80
# Height: 180
# -- Person 2 --
# Name: Mike Davis
# Age: 45
# Weight: 82
# Height: 185
# -- Person 3 --
# Name: Anna Johnson
# Age: 33
# Weight: 67
# Height: 167