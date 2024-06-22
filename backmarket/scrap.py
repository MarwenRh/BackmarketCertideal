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

def get_text_if_not_none(e):
    if e:
        return e.get_text(strip=True)
    return None

def extract_product_page_infos(html):
    products_info = []
    products_V1 = []

    bs = BeautifulSoup(html, "html5lib")
    product_elements = bs.select("div.productCard")

    print(f"Found {len(product_elements)} products.")

    for product in product_elements:
        title_11 = product.find("h2", class_="body-1-bold")
        description = get_text_if_not_none(product.find("span", class_="overflow-ellipsis overflow-hidden line-clamp-1 text-primary body-2-light"))
        evaluation = get_text_if_not_none(product.find("span", class_="ml-1 body-3-light text-primary"))
        new_prix = get_text_if_not_none(product.find("span", class_="text-primary body-2-bold"))
        old_prix = get_text_if_not_none(product.find("span", class_="text-primary-light line-through body-2-light"))
        photos = [img['src'] for img in product.find_all('img', class_="h-auto max-w-full max-h-full block mx-auto md:w-[13.8rem] w-[8.8rem]")]
        product_link = product.find('a')['href']
        color_elements = product.select('ul.flex.items-center.justify-center.list-none.mt-1 li div[role="img"]')
        colors = [color_element['style'].split('background:')[1].strip(';') for color_element in color_elements]
        product_id = product_link.split('/')[3]


        # Création d'une instance de ProductV1 avec les données extraites
        product_instance = ProductV1(
            id=product_id,
            title=get_text_if_not_none(title_11),
            price_new=new_prix,
            price_default=old_prix,
            state=description,
            rating=evaluation,
            url=product_link,
            photos=photos,
            colors=colors
        )

        # Ajout de l'instance à la liste des produits
        products_V1.append(product_instance)

    return products_V1

def main():
    url = "https://www.backmarket.fr/fr-fr/l/smartphones/6c290010-c0c2-47a4-b68a-ac2ec2b64dca"
    page = 0
    has_content = True
    infos = []
    while has_content:
        dynamic_url = url if page == 0 else url + "?page=" + str(page)
        print("Fetching URL:", dynamic_url)
        response = requests.get(dynamic_url)
        page += 1
        if response.status_code == 200:
            html = response.text
            with open("scraping-browser.html", "w", encoding='utf-8') as f:
                f.write(html)

            print("Extracting infos...")
            new_products = extract_product_page_infos(html)
            if len(new_products):
                infos.extend(new_products)
                print([product.__dict__ for product in new_products])  # Affiche les informations des produits
            else:
                has_content = False
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    if len(infos) > 0:
        with open("product_infos.json", "w", encoding='utf-8') as json_file:
            json.dump([product.__dict__ for product in infos], json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
