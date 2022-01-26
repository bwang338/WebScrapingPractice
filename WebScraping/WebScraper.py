import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

all_products = []

products = soup.select('div.thumbnail')
for product in products:
    # TODO: Work
    name = product.select('a.title')[0].text.strip()
    price = product.select('div.caption')[0].text.strip()
    desc = product.select('p.description')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    img = product.select('img')[0].get('src')
    
    all_products.append({
            "name": name,
            "description": desc,
            "price": price,
            "reviews": reviews,
            "image": img
        })

keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)


