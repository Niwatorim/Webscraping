from bs4 import BeautifulSoup
import requests
import re

url='https://sunnah.com/bukhari/1'

result = requests.get(url) #this will give us document's html file in txt format
doc = BeautifulSoup(result.text, 'html.parser')
#print(doc.prettify())

matches= doc.find_all(string=re.compile(r'Umar\s*bin\s*Al-Khattab')) #using re to find hidden spaces etc.

for match in matches:
    print(match.strip())

#to find parent: use match[0].parent etc.

#searching for tags:
result = doc.find('option')
result['value'] = 'false' #setting a tag attribute
print(result.attrs) #find all the attributes of a tag
tag = doc.find_all(['p','div']) #find multiple tags, can also do combinations of stuff

#can also combo these together, for example:
tags = doc.find_all(['option'], text='Undergraduate ') #so finds all the undergraduate tags with text of undergraduate
#can also be used for attributes

#find class names (class is a reserved value for python, so to search for class attribute, use class_)

#you can limit searches via: find_all(....., limit = n), will return n searches