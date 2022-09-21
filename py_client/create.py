import requests


headers ={'Authorization': 'Bearer'
                           '7b74944a684ddd21a1d90764468540adbefed84d'}

endpoint = "http://localhost:8000/api/products/"
data ={
    "title": "this field is done",
    "price": 400.00
}
get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())