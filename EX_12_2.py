import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


url = input('Enter  URL please - ')
# url = ('http://py4e-data.dr-chuck.net/comments_42.html')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")
tags = soup('span')

numlist = list()
for tag in tags:
    line = tag.decode()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        numlist.append(int(number))
print(sum(numlist))











