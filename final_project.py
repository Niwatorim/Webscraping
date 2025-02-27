from bs4 import BeautifulSoup
import requests
import re

url='https://sunnah.com/bukhari/1'

result = requests.get(url) #this will give us document's html file in txt format
doc = BeautifulSoup(result.text, 'html.parser')
#print(doc.prettify())

matches= doc.find_all(string=re.compile(r'Umar\s*bin\s*Al-Khattab', re.IGNORECASE)) #using re to find hidden spaces etc.

for match in matches:
    parent= match.find_parent('div', class_='english_hadith_full')
    if parent:
        hadith_text=parent.find('div',class_='text_details').get_text(strip=True)
        print(hadith_text)
