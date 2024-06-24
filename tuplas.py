# 19. Crear una tupla
def create_tuple(*args):
    return tuple(args)

# 20. Append (añadir un elemento al final de la tupla)
def append_to_tuple(tpl, element):
    return tpl + (element,)

# 21. Reverse (invertir el orden de la tupla)
def reverse_tuple(tpl):
    return tpl[::-1]

# 22. Extend (añadir varios elementos al final de la tupla)
def extend_tuple(tpl, elements):
    return tpl + tuple(elements)

# 23. Remove (eliminar la primera ocurrencia de un valor específico)
def remove_from_tuple(tpl, element):
    lst = list(tpl)
    lst.remove(element)
    return tuple(lst)

# 24. Clear (vaciar la tupla)
def clear_tuple(tpl):
    return ()

# Ejemplos de uso
if __name__ == "__main__":
    # Crear una tupla
    tpl = create_tuple(1, 2, 3)
    print("Tupla creada:", tpl)
    
    # Append
    tpl = append_to_tuple(tpl, 4)
    print("\nDespués de append (añadir 4):", tpl)
    
    # Reverse
    print("\nReverse tuple (tupla invertida):", reverse_tuple(tpl))
    
    # Extend
    tpl = extend_tuple(tpl, [5, 6])
    print("\nDespués de extend (añadir [5, 6]):", tpl)
    
    # Remove
    tpl = remove_from_tuple(tpl, 3)
    print("\nDespués de remove (eliminar la primera ocurrencia de 3):", tpl)
    
    # Clear
    tpl = clear_tuple(tpl)
    print("\nDespués de clear (vaciar la tupla):", tpl)
