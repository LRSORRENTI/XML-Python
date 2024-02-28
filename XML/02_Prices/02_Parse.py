import xml.etree.ElementTree as ET

myTree = ET.parse('01_Price.xml')
myRoot = myTree.getroot()
print(myRoot)
# <Element 'metadata' at 0x00000189FC84D210>
data = '''
    <metadata>
     <food>
        <item name="breakfast">
            Eggs
        </item>
        <price>
            $2
        </price>
        <description>
            Farm raised eggs
        </description>
        <calories>
            100
        </calories>
    </food>
    </metadata>
'''

root = ET.fromstring(data)
for data in myRoot.findall('food'):
    item = data.find('item').text
    price = data.find('price').text 
    desc = data.find('description').text
    cals = data.find('calories').text
    print(item, price, desc, cals)


