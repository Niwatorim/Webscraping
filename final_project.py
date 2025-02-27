from bs4 import BeautifulSoup
import requests
import re

url = 'https://sunnah.com/bukhari/1'

result = requests.get(url)  # this will give us document's HTML file in text format
doc = BeautifulSoup(result.text, 'html.parser')
#print(doc.prettify())

# Function to clean the hadith text
def clean_text(text):
    # Remove unwanted characters such as slashes, carriage return, and newline
    text = re.sub(r'\\[\'"rn]+', '', text)  # Removes slashes and unwanted characters like '\r', '\n', etc.
    text = re.sub(r'\\', '', text)  # Removes remaining backslashes
    text.replace('    ','')
    return text.strip()

def find_one():  # how to find only one hadith based off narrator name
    matches = doc.find_all(string=re.compile(r'Umar\s*bin\s*Al-Khattab', re.IGNORECASE))  # using re to find hidden spaces etc.

    for match in matches:
        parent = match.find_parent('div', class_='english_hadith_full')
        if parent:
            hadith_text = parent.find('div', class_='text_details').get_text(strip=True)
            cleaned_text = clean_text(hadith_text)  # Clean the extracted text
            print(cleaned_text)

# Extract all hadith and clean them
all_hadith = doc.find_all('div', class_='text_details')
coupled = {}
for hadith in all_hadith:
    text = hadith.get_text().strip()
    cleaned_text = clean_text(text)  # Clean the extracted text
    narrator = hadith.find_previous_sibling('div', class_='hadith_narrated').get_text()
    coupled[narrator] = cleaned_text  # Store cleaned hadith text

print(coupled)
