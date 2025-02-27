#for docs in directory

from bs4 import BeautifulSoup #use beautiful soup 4

with open('index.html','r') as file:
    doc =BeautifulSoup( file ,'html.parser') #parses it as html

print(doc.prettify()) #prettify makes it the indentation


#finding only one tag
first_tag = doc.title #this only gives the first item with this tag
#can modify the document too by doing first_tag.string = 'hello', will change the html itself
print(first_tag) #if i use first_tag.string it only gives the data inside the tags


#finding all tags
tags= doc.find_all('p') #finds all items with tag of 'p'
print(tags) #actually puts them in an array type format, so to get first p tag for example, just do tags[0]


#finding nested tag
nested = doc.find_all('p')[0] #need to do this cuz find_all alone is a list
print(nested.find_all('b'))
