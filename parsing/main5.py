import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www.kivano.kg'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = (response.text, 'lxml')
    return soup

def get_product_info(product:BS) -> dict:
    title = product.find('div', {'class':'listbox_title'}).text
    print(title)

def get_all_products_from_page(url:str):
    soup = get_soup(url)
    # print(soup)
    box = soup.find('div', {'class':'list-view'})
    print(box)
    # products = box.find_all('div', {'class':'product_listbox'})
#   # print(len(products))
    for product in products:
        get_product_info(product)


def main():
    category = '/noutbuki'
    get_all_products_from_page(BASE_URL + category)

main()

# Должны выйти только названия