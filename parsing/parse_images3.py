import requests, json

with open('db.json') as file:
    res = json.load(file)

# for k,v in res.items():
#     for i in v:
#         response = requests.get(i['image'])
#         for z in range(1, 4):
#             with open('images/testX'+str(z) + '.jpg', 'wb') as file:
#                 file.write(response.content)


# for z in range(1, 4):
#     file = open('images/testX'+str(z) + '.jpg', 'wb')
# for k,v in res.items():
#     for i in v:
#             response = requests.get(i['image'])
#             file.write(response.content)
#             file.close()

list_ = []
for v in res.values():
    for i in v:
        response = i['image']
        list_.append(response)
# print(list_)

enum = enumerate(list_, 1)
dict_ = dict(enum)

# for k,v in dict_.items():
#     response = requests.get(v)
#     with open('images/testX'+str(k) + '.jpg', 'wb') as file:
#         file.write(response.content)




# aaa = {2842: 'https://www.kivano.kg/images/product/101209/1638958844_77382600.png', 2843: 'https://www.kivano.kg/images/product/97157/1630651102_09623000.jpg', 2844: 'https://www.kivano.kg/images/product/117390/1677232253_64192400.png', 2845: 'https://www.kivano.kg/images/product/117391/1677232231_86118500.png', 2846: 'https://www.kivano.kg/images/product/117395/1677232212_55473700.png', 2847: 'https://www.kivano.kg/images/product/117396/1677232185_01422200.png', 2848: 'https://www.kivano.kg/images/product/117397/1677232163_22798200.png', 2849: 'https://www.kivano.kg/images/product/94390/1623838527_72512500.jpg', 2850: 'https://www.kivano.kg/images/product/89785/1615435456_73546800.png', 2851: 'https://www.kivano.kg/images/product/93115/1622087712_05276300.png', 2852: 'https://www.kivano.kg/images/product/102872/1643264458_11470400.png', 2853: 'https://www.kivano.kg/images/product/99550/1634805653_83498400.jpg'}

# for k,v in aaa.items():
#         response = requests.get(v)
#         with open('images/testX'+str(k) + '.jpg', 'wb') as file:
#             file.write(response.content)
