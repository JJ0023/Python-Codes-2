import urllib.request , urllib.parse , urllib. error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count = 0;
url = input('Enter URL')

html = urllib.request.urlopen(url).read()

stuff = ET.fromstring(html)
lst = stuff.findall('comments/comment')
print('User Count:',len(lst))
for item in lst:
    count = count + int(item.find('count').text)
print(count)