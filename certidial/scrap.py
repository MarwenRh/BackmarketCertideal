import requests
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ProductV1:
    id: Optional[str] = None
    title: Optional[str] = None
    price_default: Optional[str] = None
    price_new: Optional[str] = None
    state: Optional[str] = None
    warranty: Optional[str] = None
    rating: Optional[str] = None
    rating_count: Optional[str] = None
    url: Optional[str] = None
    photos: Optional[List[str]] = None
    colors: Optional[List[str]] = None

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0"}

def get_text_if_not_none(e):
    if e:
        return e.get_text(strip=True)
    return None

def extract_product_page_infos(html):
    products_V1 = []

    bs = BeautifulSoup(html, "html5lib")
    product_elements = bs.select("div.thumbnail")

    print(f"Found {len(product_elements)} products.")

    for product in product_elements:
        title = get_text_if_not_none(product.find("h2", class_="product-title"))
        description = get_text_if_not_none(product.find("span", class_="label-round label-state_id_99"))
        evaluation = get_text_if_not_none(product.find("span", class_="ml-1 body-3-light text-primary"))
        new_prix = get_text_if_not_none(product.find("span", class_="product-price our-price"))
        price_before = get_text_if_not_none(product.find("span", class_="product-price strike-price"))
        prices = [price.get_text(strip=True) for price in product.find_all('span', class_='product-price strike-price')]
        product_link = product.find('a')['href']
        color_elements = product.select('div.product-feature-color')
        colors = [color_element['style'].split('background:')[1].strip(';') for color_element in color_elements]
        product_id = product_link.split('/')[3]

        # Extraction des URL des photos
        images = []
        for img in product.find_all('img', class_="img-responsive center-block lazy-placeholder"):
            img_src = img.get('src')
            if not img_src:
                img_src = img.get('data-src')
            if img_src:
                images.append(img_src)

# Extraction des couleurs
        color_elements = product.select('div.product-feature-color .inner-circle')
        colors = [color_element['style'].split('background-color:')[1].strip(';') for color_element in color_elements]
        product_id = product_link.split('/')[3]
       


        # Création d'une instance de ProductV1 avec les données extraites
        product_instance = ProductV1(
            id=product_id,
            title=title,
            price_new=new_prix,
            price_default=price_before,
            state=description,
            rating=evaluation,
            url=product_link,
            photos=images,
            colors=colors
        )

        # Ajout de l'instance à la liste des produits
        products_V1.append(product_instance)

    return products_V1

def main():
    base_url = "https://certideal.com/iphone-reconditionnes-82"
    page = 1
    has_content = True
    infos = []

    while has_content:
        dynamic_url = base_url if page == 1 else f"{base_url}?page={page}"
        print("Fetching URL:", dynamic_url)
        
        response = requests.get(dynamic_url, headers=HEADERS)
        if response.status_code == 200:
            html = response.text
            new_products = extract_product_page_infos(html)
            
            if new_products:
                infos.extend(new_products)
                
                for product in new_products:
                    print(json.dumps(product.__dict__, ensure_ascii=False, indent=4))
                page += 1
            else:
                has_content = False
        else:
            print("ERREUR:", response.status_code)
            has_content = False

    if infos:
        with open("product_infos.json", "w", encoding='utf-8') as json_file:
            json.dump([product.__dict__ for product in infos], json_file, ensure_ascii=False, indent=4)
    else:
        print("No products found.")

if __name__ == '__main__':
    main()
