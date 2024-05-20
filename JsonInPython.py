import json

# 1. Leer el archivo JSON y mostrar todos los productos
with open('products.json') as f:
    data = json.load(f)

print("Todos los productos:")
for product in data:
    print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']}")

# 2. Agregar un nuevo producto
new_product = {
    "id": 7,
    "name": "Microsoft Surface Laptop 5",
    "price": 1800
}

data.append(new_product)

with open('products.json', 'w') as f:
    json.dump(data, f)

print("\nProducto agregado:")

# Imprimir todos los productos actualizados
for product in data:
    print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']}")

# 3. Actualizar el precio de un producto existente
for product in data:
    if product['id'] == 1:  # Supongamos que queremos actualizar el precio del producto con ID 1
        product['price'] = 1700

with open('products.json', 'w') as f:
    json.dump(data, f)

print("\nPrecio actualizado:")

# Imprimir todos los productos actualizados
for product in data:
    print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']}")

# 4. Eliminar un producto
data = [product for product in data if product['id'] != 2]  # Eliminar el producto con ID 2

with open('products.json', 'w') as f:
    json.dump(data, f)

print("\nProducto eliminado:")

# Imprimir todos los productos actualizados
for product in data:
    print(f"ID: {product['id']}, Nombre: {product['name']}, Precio: ${product['price']}")
