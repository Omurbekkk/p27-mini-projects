import requests
from bs4 import BeautifulSoup


main_url = 'https://www.kivano.kg/'

response = requests.get(main_url)

# response = requests.get(main_url)  # отправляем запрос
# print(response.text)  # html - str 

soup = BeautifulSoup(response.text, 'lxml')
# print(dir(soup))

phones_span = soup.find('span', {'id':'phones'})
# print(phones_span.text)
raw_phones = phones_span.text
phones_list = []

for ph in raw_phones.split('\n'):
    # print(repr(ph))
    clear_phone = ph.replace('\r', '').strip()
    # print(repr(clear_phone))
    if clear_phone:
        phones_list.append(clear_phone)

# print(phones_list)

# python3 main.py




'====================Детализация продукта================='


product_url = 'product/view/sotovyy-telefon-apple-iphone-14-pro-256gb-fioletovyy'

response = requests.get(main_url+product_url)  # ...200
# print(response)

soup = BeautifulSoup(response.text, 'lxml')

product_card = soup.find('div', {'class':'product-view'})
# print(product_card)

title = product_card.find('h1')
# print(title)
#  целый тег, как в html
# <h1 itemprop="name" style="margin-left:15px; margin-bottom:5px;">Сотовый телефон Apple iPhone 14 Pro 256GB фиолетовый</h1>


title = product_card.find('h1').text
# print(title)
# Сотовый телефон Apple iPhone 14 Pro 256GB фиолетовый


# print(product_card.find_all('img'))
# Действительно ли что мы ищем в единств экземпляре
# Если 1 файл то можно просто find

image_box = product_card.find('div', {'class':'img_full'})
# print(image_box.find_all('img'))

image = image_box.find('img').get('src')  #  С пом-ю get вытащили именно ссылку из тега
# print(image)


price = product_card.find('span', {'itemprop':'price'}).text
# print(price)

data = {'title':title, 'image':image, 'price':price}
print(data)

















