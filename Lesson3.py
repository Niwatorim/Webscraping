#navigating through html trees
from bs4 import BeautifulSoup
import requests

url='https://coinmarketcap.com/'
result=requests.get(url).text
doc=BeautifulSoup(result,'html.parser')

tbody = doc.tbody #can just focus on the tbody tags
trs = tbody.contents #gives all the contents inside the tbody, like making mini doc

'''
#working with siblings
print(trs[0].next_sibling) #gives me the second sibling element
print(trs[0].next_siblings) #gives all the other siblings
print(trs[0].descendants) #can also write .children or .contents
'''

#grabbing crypto currency prices
prices={}
for tr in trs[:10]: #top ten names
    name,price =  tr.contents[2:4] #we skip 4 as we want to only get names and prices
    fixed_name= name.p.string
    fixed_price=price.a.string
    prices[fixed_name] = fixed_price

print(prices)
