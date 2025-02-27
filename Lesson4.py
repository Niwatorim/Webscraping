from bs4 import BeautifulSoup
import requests
import re

gpu = input("what product should be searched for")  # Taking user input for the product search
url = f'https://www.newegg.com/global/ae-en/p/pl?d={gpu}&N=4131'  # Formatting URL with the searched product

# Adding headers to avoid bot detection
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

page = requests.get(url, headers=headers).text
doc = BeautifulSoup(page, 'html.parser')

# Finding the pagination element
pagination_element = doc.find(class_="list-tool-pagination-text")

if pagination_element:
    page_text = pagination_element.find('strong')  # Extract the text inside the pagination element
    pages = str(page_text).split('/')[-2]  # Since we get two slashes, we want the content in the middle
    max_page = int(pages.split('>')[-1][:-1])  # Removes the last item and converts it to an integer
else:
    print("Pagination element not found. Assuming only one page.")  # If no pagination exists, assume only 1 page
    max_page = 1

# Creating dictionary for all the content
items_found = {}

for page_num in range(1, max_page + 1):
    url = f'https://www.newegg.com/global/ae-en/p/pl?d={gpu}&N=4131&page={page_num}'  # Cycles through the pages and sends a new request to all of them
    page = requests.get(url, headers=headers).text
    doc = BeautifulSoup(page, 'html.parser')

    # How to find only the GPU that I want (not anything unnecessary)
    div = doc.find(class_="item-cells-wrap border-cells short-video-box items-list-view is-list")

    if not div:
        print(f"No items found on page {page_num}.")
        continue

    items = div.find_all(string=re.compile(gpu, re.IGNORECASE))  # Using re.compile allows for any content with the words of GPU in them (case insensitive)

    for item in items:
        parent = item.parent  # Getting the parent element

        if parent.name != 'a':  # Ensuring it's a link
            continue
        
        link = parent['href']  # Extracting the product link

        next_parent = item.find_parent(class_='item-container')  # Finding the container with the price

        if not next_parent:
            continue

        price_element = next_parent.find(class_='price-current')  # Finding the price section
        if not price_element:
            continue

        price_strong = price_element.find('strong')  # Extracting the main price
        if not price_strong:
            continue

        price = price_strong.string  # Getting the price as a string

        # Storing the found GPU information
        items_found[item] = {'price': int(price.replace(',', '')), 'link': link}

# Sorting the items by price
sorted_items = sorted(items_found.items(), key=lambda x: x[1]['price'])
#sorted- sorts list by specific key
#x[1] gets the difctionary
#x[1]['price'] gets the price section only
#to do descending just write reverse=True at end of sort function


# Printing the sorted results
for item in sorted_items:
    print(item[0])
    print(f'${item[1]["price"]}')
    print(item[1]["link"])
    print('---------------')
