from bs4 import BeautifulSoup
import urllib2
import pprint
import json

pp = pprint.PrettyPrinter(indent=4)

print("Fetching the data....")

response = urllib2.urlopen('https://github.com/sindresorhus/amas/blob/master/readme.md')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

article = soup.find('article')
ul = article.find('ul')
li = ul.find_all('li')

arr = []
for item in li:
	link = item.find('a')['href']
	fullname = item.find('a').string
	username = link.split('/')[3]
	description = item.find('a').next_sibling
	obj = {
		"username": username,
		"link": link,
		"fullname": fullname,
		"description": description
	}
	arr.append(obj)

# pp.pprint(arr)
print("Data Stored in `amas.json` file")

with open('amas.json', 'w') as outfile:
  json.dump(arr, outfile, indent=4, sort_keys=True, separators=(',', ':'))