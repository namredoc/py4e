import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter  URL please - ')
# url = ('http://py4e-data.dr-chuck.net/known_by_Fikret.html')
html = urllib.request.urlopen(url).read()

position = int(input('Enter position: '))-1
count = int(input('Enter count: '))-1
# soup = BeautifulSoup(html, 'html.parser')

print(url)

# Reminder tags comes as list

while count >=  0:
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position].get('href', None)
    count = count - 1    
    print(url)


