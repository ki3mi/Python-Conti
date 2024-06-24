# 25. Crear un diccionario
def create_dict(**kwargs):
    return dict(kwargs)

# 26. Get (obtener el valor asociado a una clave)
def get_from_dict(dct, key, default=None):
    return dct.get(key, default)

# 27. Keys (obtener todas las claves del diccionario)
def get_keys(dct):
    return dct.keys()

# 28. Values (obtener todos los valores del diccionario)
def get_values(dct):
    return dct.values()

# 29. Items (obtener todos los pares clave-valor del diccionario)
def get_items(dct):
    return dct.items()

# 30. Pop (eliminar un par clave-valor y devolver el valor)
def pop_from_dict(dct, key):
    return dct.pop(key, None)

# 31. Popitem (eliminar y devolver el último par clave-valor)
def popitem_from_dict(dct):
    return dct.popitem()

# 32. Del (eliminar un par clave-valor)
def delete_from_dict(dct, key):
    if key in dct:
        del dct[key]
    return dct

# 33. Clear (vaciar el diccionario)
def clear_dict(dct):
    dct.clear()
    return dct

# 34. Hash (obtener el hash de una clave, si es posible)
def get_hash(key):
    try:
        return hash(key)
    except TypeError:
        return None

# Ejemplos de uso
if __name__ == "__main__":
    # Crear un diccionario
    dct = create_dict(a=1, b=2, c=3)
    print("Diccionario creado:", dct)
    
    # Get
    print("\nGet 'a':", get_from_dict(dct, 'a'))
    print("Get 'z' (con valor por defecto):", get_from_dict(dct, 'z', 'default'))
    
    # Keys
    print("\nKeys del diccionario:", list(get_keys(dct)))
    
    # Values
    print("\nValues del diccionario:", list(get_values(dct)))
    
    # Items
    print("\nItems del diccionario:", list(get_items(dct)))
    
    # Pop
    print("\nPop 'b':", pop_from_dict(dct, 'b'))
    print("Después de pop:", dct)
    
    # Popitem
    print("\nPopitem (eliminar y devolver el último par):", popitem_from_dict(dct))
    print("Después de popitem:", dct)
    
    # Del
    dct = create_dict(a=1, b=2, c=3)
    dct = delete_from_dict(dct, 'c')
    print("\nDespués de del 'c':", dct)
    
    # Clear
    dct = clear_dict(dct)
    print("\nDespués de clear (vaciar el diccionario):", dct)
    
    # Hash
    print("\nHash de 'a':", get_hash('a'))
    print("Hash de [1, 2, 3] (no hashable):", get_hash([1, 2, 3]))