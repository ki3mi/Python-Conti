from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

data = [
            {
                "id": 1,
                "name": "RTX 4060",
                "price": 1600
            },
            {
                "id": 2,
                "name": "iPhone 15 Pro",
                "price": 1500
            },
            {
                "id": 3,
                "name": "Samsung Galaxy Fold 4",
                "price": 2000
            },
            {
                "id": 4,
                "name": "Dell XPS 17",
                "price": 2200
            },
            {
                "id": 5,
                "name": "Sony A9 III",
                "price": 5000
            },
            {
                "id": 6,
                "name": "Bose Noise Cancelling Headphones 900",
                "price": 400
            }
        ]
app = FastAPI()

class Product(BaseModel):
    name:str
    price:float
# Index
@app.get("/")
def index():
    return{"Hola xd"}

# Get products
@app.get("/products")
def products():
    return data

# Actualizar producto
@app.put("/edit/{id}")
def update_product(id: int, product: Product):
    for producto in data:
        if producto["id"] == id:
            producto.update(product)
    return {"name":product.name, "id":id}