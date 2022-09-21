import requests


endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": " Hello world my old friend",
    "price": 420.00
}

get_response = requests.put(endpoint, json=data)# HTTP Request

print(get_response.json())