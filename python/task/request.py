import requests

response = requests.get("https://dummyjson.com/products")

data = response.json()

for product in data["products"]:
    data = f"id : {product['id']} name : {product["title"]} description : {product["description"]} price : {product["price"]}\n" 
    with open("python/task/data.txt","a") as file:
     file.write(data)
     
    

