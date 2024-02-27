# Python has built in modules for handling XML 
import xml.sax 

# First set up a handler:
handler = xml.sax.ContentHandler()
# Second set up a parser:
parser = xml.sax.make_parser()
# Third set the content handler to the handler:
parser.setContentHandler(handler)
# Then pass in the xml file to parser.parse:
parser.parse('people.xml')