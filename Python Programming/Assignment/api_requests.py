import requests

# Base URL for the API endpoint
base_url = "http://127.0.0.1:5000/items"

# GET Request
response = requests.get(base_url)
print("GET Request Response:")
print(response.json())

# POST Request
data_to_post = {"id": 3, "name": "Item 3"}
response = requests.post(base_url, json=data_to_post)
print("\n POST Request Response:")
print(response.json())

# DELETE Request
data_to_delete = {"id": 1}  # Specify the ID of the item to delete
response = requests.delete(base_url, json=data_to_delete)
print("\n DELETE Request Response:")
print(response.json())

# GET Request after deletion
response = requests.get(base_url)
print("\nGET Request Response after deletion:")
print(response.json())
