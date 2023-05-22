# Crear una tupla
mi_tupla = (1, 2, 3, 'Hola', 'Mundo')

# Acceder a elementos de una tupla
print(mi_tupla[0])  # Salida: 1
print(mi_tupla[3])  # Salida: 'Hola'

# Longitud de una tupla
print(len(mi_tupla))  # Salida: 5

# Iterar sobre una tupla
for elemento in mi_tupla:
    print(elemento)

# Convertir una tupla en una lista
lista = list(mi_tupla)

# Acceder a un rango de elementos de una tupla (slice)
sub_tupla = mi_tupla[1:4]
print(sub_tupla)  # Salida: (2, 3, 'Hola')

# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = ('a', 'b', 'c')
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Salida: (1, 2, 3, 'a', 'b', 'c')
