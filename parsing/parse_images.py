import requests, json

image_url = 'https://mobimg.b-cdn.net/v3/fetch/94/94c56e15f13f1de4740a76742b0b594f.jpeg'

# response = requests.get(image_url)

# def write_to_json(data:dict):
#     with open('db.json', 'w', encoding='utf-8') as file:
#         json.dump(data, file, ensure_ascii=False)

with open('db.json') as file:
    res = json.load(file)

# with open('images/test.jpg', 'wb') as file:
#     file.write(response.content)


for k,v in res.items():
    for i in v:
        response = requests.get(i['image'])
        for a in range(1,2821):
            with open('images/test111.jpg', 'wb') as file:
                file.write(response.content)

        
