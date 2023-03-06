import requests
from bs4 import BeautifulSoup


main_url = 'https://www.kivano.kg/'

response = requests.get(main_url)
# Отправили запрос
print(dir(requests))
print(dir(response))
# Потом из запроса вытащили html в виде строки    , то есть текст запроса(страницы)
soup = BeautifulSoup(response.text, 'lxml')
# Мы сделали ветвление html, чтобы мы могли работать.    И теперь работаем с soup (как со строкой)




phones_span = soup.find('span', {'id':'phones'})
# находит весь блок
# print(phones_span.text)
raw_phones = phones_span.text
# вытаскиваем текст блока

# print(raw_phones)

phones_list = []

xx = raw_phones.split('\n')

# print(xx)

for ph in xx:
    # print(repr(ph))
    # repr - делает в кавычках
    clear_phone = ph.replace('\r', '').strip()
    print(clear_phone)
    # print(repr(clear_phone))
    if clear_phone:
        phones_list.append(clear_phone)

print(phones_list)









