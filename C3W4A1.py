import urllib.request , urllib.parse , urllib. error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_138214.html').read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
sum = 0
for tag in tags:
    num = int(tag.contents[0])
    sum = sum + num
print('Sum is',sum)



