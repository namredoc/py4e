import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = input('Enter the URl, please ')
url = ('http://py4e-data.dr-chuck.net/comments_1613978.xml')
xml_data = urllib.request.urlopen(url).read()

tree = ET.fromstring(xml_data)
counts = tree.findall('.//count')

# Shows the same as comment_count
# print(len(counts))

total = 0
comment_count = 0
for comment in counts:
    number = comment.text
    number = int(number)
    total = total + number
    comment_count = comment_count + 1
print(total)
