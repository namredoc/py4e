import json
import urllib.request, urllib.parse, urllib.error
import ssl


# url = input('Enter the URl, please ')
# url = ('http://py4e-data.dr-chuck.net/comments_42.json')
url = ('http://py4e-data.dr-chuck.net/comments_1613979.json')
url_handle = urllib.request.urlopen(url)
data = url_handle.read()

print('Retieving url', url)
print('Retrieved', len(data), 'characters')

info = json.loads(data)
info = info['comments']
print('User count:', len(info))

comment_count = 0
total = 0
for comment in info:
	number = int((comment['count']))
	total = total + number

	comment_count = comment_count + 1
print('Comment count', comment_count)
print(total)
