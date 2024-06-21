import re
import json
import os
import time
import inspect
import pycurl
from io import BytesIO
from bs4 import BeautifulSoup
from typing import Optional, List
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

def clean_price(price):
    # Remove non-breaking spaces and other unwanted whitespace characters
    cleaned_price = re.sub(r'\s+', ' ', price).strip()
    # Remove any currency symbols (€, $, etc.)
    cleaned_price = re.sub(r'[^\d,\.]', '', cleaned_price)
    return cleaned_price

buffer = BytesIO()

curl = pycurl.Curl()
curl.setopt(pycurl.URL, 'https://www.backmarket.fr/fr-fr/l/iphone-reconditionne/aabc736a-cb66-4ac0-a3b7-0f449781ed39')
curl.setopt(pycurl.WRITEDATA, buffer)
curl.perform()
curl.close()

soup = BeautifulSoup(buffer.getvalue(), 'html.parser')

product_cards = soup.select("div.productCard")

@dataclass
class ProductV1:
    id: Optional[str] = None
    title_element: Optional[str] = None
    current_price: Optional[str] = None
    price_before: Optional[str] = None
    state: Optional[str] = None
    warranty: Optional[str] = None
    rating_element: Optional[str] = None
    number_of_ratings: Optional[str] = None
    product_url: Optional[str] = None
    photos: Optional[List[str]] = None
    colors: Optional[List[str]] = None

# Liste pour stocker les produits
products_V1 = []

for card in product_cards:
    title_element = card.find("h2", class_="body-1-bold")
    current_price = card.find("span", class_="text-primary body-2-bold")
    price_before = card.find("span", class_="text-primary-light line-through body-2-light")
    warranty = card.find("span", string=lambda x: x and "Garantie commerciale" in x)
    rating_element = card.find("span", class_="ml-1 text-primary body-2-bold")
    number_of_ratings = card.find("span", class_="ml-1 body-3-light text-primary")
    product_link = card.find('a')['href']
    photos = [img['src'] for img in card.find_all('img', class_="h-auto max-w-full max-h-full block mx-auto md:w-[13.8rem] w-[8.8rem]")]  # Extraction des URL des photos
    
    # Extraction des couleurs
    color_elements = card.select('ul.flex.items-center.justify-center.list-none.mt-1 li div[role="img"]')
    colors = [color_element['style'].split('background:')[1].strip(';') for color_element in color_elements]

    # Extraction de l'ID à partir de l'URL du produit
    product_id = product_link.split('/')[3]

    if price_before:
        price_before_text = clean_price(price_before.text.strip())
        price_parts = price_before_text.split('neuf')
        price_before = price_parts[0].strip() if price_parts[0] else "Not found"
        state = 'new' if len(price_parts) > 1 else "Not found"
    else:
        price_before = "Not found"
        state = "Not found"
    
    rating_element_text = rating_element.text.strip() if rating_element else "Not found"
    if rating_element != "Not found":
        rating_average = rating_element_text.split('/5')
        rating_element = rating_average[0].strip() if rating_average else "Not found"
    
    number_of_ratings_text = number_of_ratings.text.strip() if number_of_ratings else "Not found"
    number_of_ratings_text = number_of_ratings_text.replace("(", "").replace(")", "")  # Enlever les parenthèses

    warranty_text = warranty.text.strip().replace("Garantie commerciale :", "").strip() if warranty else "Not found"
    warranty_duration = warranty_text.split('mois')[0].strip() if 'mois' in warranty_text else warranty_text

    # Clean the current price
    current_price_text = clean_price(current_price.text.strip()) if current_price else "Not found"

    # Création d'une instance de ProductV1 avec les données extraites
    product_instance = ProductV1(
        id=product_id,
        title_element=title_element.text.strip() if title_element else "Not found",
        current_price=current_price_text,
        price_before=price_before,
        state=state,
        warranty=warranty_duration,
        rating_element=rating_element,
        number_of_ratings=number_of_ratings_text,
        product_url=product_link,
        photos=photos,
        colors=colors
    )

    # Ajout de l'instance à la liste des produits
    products_V1.append(product_instance)

# Conversion de la liste des produits en JSON
json_objectV1 = json.dumps(products_V1,
                           default=lambda o: dict((key, value) for key, value in o.__dict__.items() if value),
                           indent=4,
                           allow_nan=False,
                           ensure_ascii=False)

# Écrire le JSON dans un fichier avec des paramètres personnalisés
write_output_to_file(json_objectV1, folder_path=r'C:\Users\Lenovo\Desktop\python', file_name='mon_fichier', add_file_date=False, extension=".json")