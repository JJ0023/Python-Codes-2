import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter URL')
count = int(input('Enter Count'))
pos = int(input('Enter Position'))
position = pos-1


for i in range(count):
    print(i,'Cycle')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    li = []
    name = []
    for tag in tags:
        x = tag.get('href', None)
        li.append(x)
        y = tag.text
        name.append(y)

    print(li[position])
    print(name[position])
    url = li[position]



