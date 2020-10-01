#XML Data Parsing
import xml.etree.ElementTree as ET
input = '''
        <stuff>
        <users>
            <user x="2">
                <id>001</id>
                <name>Jeevan</name>
            </user>
            <user x = "7">
                <id>009</id>
                <name>Jyoti</name>
            </user>
        </users>
        </stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
lsti = lst
print('User Count:',len(lst))
#print('User Count:',len(lst)) is used for user count
print("Multiple comment lines skipped by Bishal")
for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:' , item.get("x"))
