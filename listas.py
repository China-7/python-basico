# Crear una lista
mi_lista = [1, 2, 3, 'Hola', 'Mundo']

# Acceder a elementos de una lista
print(mi_lista[0])  # Salida: 1
print(mi_lista[3])  # Salida: 'Hola'

# Modificar un elemento de la lista
mi_lista[1] = 'Python'

# Agregar elementos a una lista
mi_lista.append('Nuevo elemento')
mi_lista.insert(2, 'Otro elemento')

# Eliminar elementos de una lista
del mi_lista[3]  # Elimina el elemento en el índice 3
mi_lista.remove('Python')  # Elimina la primera aparición de 'Python'
elemento_eliminado = mi_lista.pop()  # Elimina y devuelve el último elemento

# Longitud de una lista
print(len(mi_lista))  # Salida: 4

# Iterar sobre una lista
for elemento in mi_lista:
    print(elemento)

# Convertir una lista en una tupla
tupla = tuple(mi_lista)

# Acceder a un rango de elementos de una lista (slice)
sub_lista = mi_lista[1:3]
print(sub_lista)  # Salida: [2, 'Otro elemento']

# Concatenar listas
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
lista_concatenada = lista1 + lista2
print(lista_concatenada)  # Salida: [1, 2, 3, 'a', 'b', 'c']
