def quicksort(lista_especialistas:list) -> list:
    """Función que ordena una lista de especialistas médicos 
    utilizando el algoritmo QuickSort."""

    if len(lista_especialistas) <= 1: # Si la lista tiene menos de 1 elemento, esta ordenada.
        return lista_especialistas
    pivote = lista_especialistas[0] # Elegimos la primer palabra como pivote (usado como refencia para dividir la lista)

    # organiza los elementos menores a un lado y los mayores al otro.
    menor = [x for x in lista_especialistas[1:] if x <= pivote]  # primero los menores
    mayor = [x for x in lista_especialistas[1:] if x > pivote]   # luego los mayores
    return quicksort(menor) + [pivote] + quicksort(mayor) # retornamos la lista con los elementos y el pivote

# Busqueda binaria

def busqueda_binaria(lista: list, objetivo: str) -> int:
    """Función que realiza una búsqueda binaria en una lista ordenada."""
    
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
