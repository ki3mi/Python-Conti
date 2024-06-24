# 35. Crear un conjunto
def create_set(*args):
    return set(args)

# 36. Add (añadir un elemento al conjunto)
def add_to_set(st, element):
    st.add(element)
    return st

# 37. Remove (eliminar un elemento del conjunto, genera un error si no existe)
def remove_from_set(st, element):
    st.remove(element)
    return st

# 38. Discard (eliminar un elemento del conjunto, no genera un error si no existe)
def discard_from_set(st, element):
    st.discard(element)
    return st

# 39. Sorted (devolver una lista ordenada de los elementos del conjunto)
def sorted_set(st):
    return sorted(st)

# 40. Intersección (devolver la intersección de dos conjuntos)
def intersection_of_sets(st1, st2):
    return st1.intersection(st2)

# 41. Unión (devolver la unión de dos conjuntos)
def union_of_sets(st1, st2):
    return st1.union(st2)

# 42. Diferencia (devolver la diferencia de dos conjuntos)
def difference_of_sets(st1, st2):
    return st1.difference(st2)

# 43. Diferencia simétrica (devolver la diferencia simétrica de dos conjuntos)
def symmetric_difference_of_sets(st1, st2):
    return st1.symmetric_difference(st2)

# 44. Inclusión (comprobar si un conjunto es subconjunto de otro)
def is_subset(st1, st2):
    return st1.issubset(st2)

# 45. Crear un frozenset
def create_frozenset(*args):
    return frozenset(args)

# Ejemplos de uso
if __name__ == "__main__":
    # Crear un conjunto
    st = create_set(1, 2, 3)
    print("Conjunto creado:", st)
    
    # Add
    st = add_to_set(st, 4)
    print("\nDespués de add (añadir 4):", st)
    
    # Remove
    try:
        st = remove_from_set(st, 2)
        print("\nDespués de remove (eliminar 2):", st)
    except KeyError:
        print("\nError: El elemento 2 no se encuentra en el conjunto")

    # Discard
    st = discard_from_set(st, 5)
    print("\nDespués de discard (descartar 5):", st)
    
    # Sorted
    print("\nSorted set (conjunto ordenado):", sorted_set(st))
    
    # Intersección
    st2 = create_set(3, 4, 5)
    print("\nIntersección con {3, 4, 5}:", intersection_of_sets(st, st2))
    
    # Unión
    print("\nUnión con {3, 4, 5}:", union_of_sets(st, st2))
    
    # Diferencia
    print("\nDiferencia con {3, 4, 5}:", difference_of_sets(st, st2))
    
    # Diferencia simétrica
    print("\nDiferencia simétrica con {3, 4, 5}:", symmetric_difference_of_sets(st, st2))
    
    # Inclusión
    st3 = create_set(1, 4)
    print("\n¿{1, 4} es subconjunto de {1, 3, 4}?:", is_subset(st3, st))
    
    # Crear un frozenset
    fst = create_frozenset(1, 2, 3)
    print("\nFrozenset creado:", fst)
