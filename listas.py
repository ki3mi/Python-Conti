# 1. Crear una lista
def create_list(*args):
    return list(args)

# 2. Append (añadir un elemento al final de la lista)
def append_to_list(lst, element):
    lst.append(element)
    return lst

# 3. Extend (añadir varios elementos al final de la lista)
def extend_list(lst, elements):
    lst.extend(elements)
    return lst

# 4. Insert (insertar un elemento en una posición específica)
def insert_to_list(lst, index, element):
    lst.insert(index, element)
    return lst

# 5. Delete (eliminar un elemento en una posición específica)
def delete_from_list(lst, index):
    del lst[index]
    return lst

# 6. Remove (eliminar la primera ocurrencia de un valor específico)
def remove_from_list(lst, element):
    lst.remove(element)
    return lst

# 7. Reversed (invertir el orden de la lista)
def reverse_list(lst):
    return list(reversed(lst))

# 8. Sort (ordenar la lista en su lugar)
def sort_list(lst):
    lst.sort()
    return lst

# 9. Sorted (devolver una nueva lista ordenada)
def sorted_list(lst):
    return sorted(lst)

# 10. Concatenar dos listas
def concatenate_lists(lst1, lst2):
    return lst1 + lst2

# 11. Replicar una lista
def replicate_list(lst, times):
    return lst * times

# 12. Trocear (cortar una lista en un rango específico)
def slice_list(lst, start, end):
    return lst[start:end]

# 13. Min (encontrar el valor mínimo en la lista)
def min_in_list(lst):
    return min(lst)

# 14. Max (encontrar el valor máximo en la lista)
def max_in_list(lst):
    return max(lst)

# 15. Index (encontrar el índice de la primera ocurrencia de un valor)
def index_in_list(lst, element):
    return lst.index(element)

# 16. Count (contar el número de ocurrencias de un valor)
def count_in_list(lst, element):
    return lst.count(element)

# 17. Sum (sumar todos los elementos de la lista)
def sum_of_list(lst):
    return sum(lst)

# 18. In (comprobar si un valor está en la lista)
def is_in_list(lst, element):
    return element in lst

# Ejemplos de uso
if __name__ == "__main__":
    # Crear una lista
    lst = create_list(1, 2, 3)
    print("Lista creada:", lst)
    
    # Append
    lst = append_to_list(lst, 4)
    print("\nDespués de append (añadir 4):", lst)
    
    # Extend
    lst = extend_list(lst, [5, 6])
    print("\nDespués de extend (añadir [5, 6]):", lst)
    
    # Insert
    lst = insert_to_list(lst, 2, 10)
    print("\nDespués de insert (insertar 10 en posición 2):", lst)
    
    # Delete
    lst = delete_from_list(lst, 2)
    print("\nDespués de delete (eliminar en posición 2):", lst)
    
    # Remove
    lst = remove_from_list(lst, 3)
    print("\nDespués de remove (eliminar la primera ocurrencia de 3):", lst)
    
    # Reversed
    print("\nReversed list (lista invertida):", reverse_list(lst))
    
    # Sort
    lst = sort_list(lst)
    print("\nDespués de sort (lista ordenada):", lst)
    
    # Sorted
    print("\nSorted list (nueva lista ordenada):", sorted_list([3, 1, 2]))
    
    # Concatenate
    print("\nConcatenate lists (concatenar con [7, 8]):", concatenate_lists(lst, [7, 8]))
    
    # Replicate
    print("\nReplicate list (replicar lista 2 veces):", replicate_list(lst, 2))
    
    # Slice
    print("\nSlice list (trocear lista de 1 a 3):", slice_list(lst, 1, 3))
    
    # Min
    print("\nMin in list (valor mínimo en la lista):", min_in_list(lst))
    
    # Max
    print("\nMax in list (valor máximo en la lista):", max_in_list(lst))
    
    # Index
    print("\nIndex in list (índice de la primera ocurrencia de 2):", index_in_list(lst, 2))
    
    # Count
    print("\nCount in list (número de ocurrencias de 2):", count_in_list(lst, 2))
    
    # Sum
    print("\nSum of list (suma de todos los elementos):", sum_of_list(lst))
    
    # In
    print("\nIs in list (comprobar si 2 está en la lista):", is_in_list(lst, 2))
