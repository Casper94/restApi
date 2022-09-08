import requests

# endpoint = " https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, params={"abc": 123}, json={"product_id": 123})
get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello World", "price": "abc123"} )# HTTP Request

# print(get_response.headers)
# print(get_response.text)
print(get_response.json())