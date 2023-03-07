import json

with open('db.json') as file:
    res = json.load(file)

# for k,v in res.items():
#     for i in v:
#         response = i['image']
#         with open('images/test111.json', 'a') as file:
#             file.write(response + '\n')

# for k,v in res.items():
#     for i in v:
#         response = i['image']
#         with open('images/test111.json', 'a') as file:
#             file.write(response)


