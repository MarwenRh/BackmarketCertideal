import re
import json
import os
import time
import inspect
import requests
from bs4 import BeautifulSoup
from typing import Optional
from dataclasses import dataclass

def write_output_to_file(data, folder_path=r'C:\Users\Lenovo\Desktop\python', file_name=None, path_includes_in_file_name=False, add_file_date=True, include_seconds_in_date=True, extension=".json"):
    if not file_name:
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__.__name__
        file_name = "{}".format(the_class)

    if add_file_date:
        timestr = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) if include_seconds_in_date else time.strftime('%Y_%m_%d_%H_%M', time.localtime(time.time()))
        file_name = file_name + "_" + timestr

    file_name = file_name + extension
    if not path_includes_in_file_name:
        path = folder_path

        def PATH(p):
            return os.path.abspath(os.path.join(os.path.dirname(__file__), p))

        if not (os.path.isdir(PATH(path))):
            os.mkdir(PATH(path))
            if not (os.access(PATH(path), os.W_OK)):
                print('Path {' + path + '} cannot be written.')

        filename = PATH(path + "/" + file_name)
    else:
        filename = file_name

    with open(filename, "w+", encoding='utf-8') as file:
        file.write(data)

@dataclass
class ProductV2:
    id: Optional[str] = None
    title: Optional[str] = None
    rating: Optional[str] = None
    rating_numbers: Optional[str] = None
    price_starting_at: Optional[str] = None
    stockage: Optional[str] = None  # Added stockage field

def fetch_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Save HTML content to a file for inspection
    with open(r'C:\Users\Lenovo\Desktop\python\product_page.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    title = soup.find("h1", {"class": "heading-1"}).text.strip() if soup.find("h1", {"class": "heading-1"}) else "Not found"
    rating = soup.find("span", {"class": "ml-4 mt-1 md:mt-2 body-2-bold"}).text.strip() if soup.find("span", {"class": "ml-4 mt-1 md:mt-2 body-2-bold"}) else "Not found"
    rating_numbers = soup.find("div", {"class": "body-2-link ml-8 underline-offset-2"}).text.strip() if soup.find("div", {"class": "body-2-link ml-8 underline-offset-2"}) else "Not found"

    # Remove parentheses from rating numbers
    if rating_numbers != "Not found":
        rating_numbers = rating_numbers.strip('()').replace('avis', '').strip()

    # Remove "/5" from rating
    if rating != "Not found":
        rating = rating.replace("/5", "").strip()

    # Find the JSON-LD script tag for price
    json_ld_script = soup.find("script", {"type": "application/ld+json"})
    price_starting_at = "Not found"
    if json_ld_script:
        try:
            json_ld_data = json.loads(json_ld_script.string)
            if 'offers' in json_ld_data and 'price' in json_ld_data['offers']:
                price_starting_at = json_ld_data['offers']['price']  # Directly use the price without currency
        except json.JSONDecodeError:
            print("Error decoding JSON-LD data")

    # Extract stockage information
    stockage = "Not found"
    stockage_element = soup.find("a", {"class": "text-action-default-hi focus-visible-outline-default-hi rounded-md font-weight-body-1-link cursor-pointer hover:text-action-default-hi-hover underline"})
    if stockage_element:
        stockage = stockage_element.text.strip()

    return ProductV2(
        id=url.split("/")[-1],  # Assuming the ID is the last part of the URL
        title=title,
        rating=rating,
        rating_numbers=rating_numbers,
        price_starting_at=price_starting_at,
        stockage=stockage  # Include the extracted stockage information
    )

# Load the initial JSON file with basic product info
with open(r'C:\Users\Lenovo\Desktop\python\mon_fichier.json', 'r', encoding='utf-8') as file:
    products_V1 = json.load(file)

# List to store detailed product information
products_V2 = []

for product in products_V1:
    product_url = product['product_url']
    full_url = f"https://www.backmarket.fr{product_url}"
    product_details = fetch_product_details(full_url)
    products_V2.append(product_details)

# Convert the list of detailed products to JSON
json_objectV2 = json.dumps(products_V2, default=lambda o: dict((key, value) for key, value in o.__dict__.items() if value), indent=4, allow_nan=False, ensure_ascii=False)

# Write the detailed product JSON to a file
write_output_to_file(json_objectV2, folder_path=r'C:\Users\Lenovo\Desktop\python', file_name='detailed_products', add_file_date=False, extension=".json")
