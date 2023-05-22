# Crear un diccionario
mi_diccionario = {
    'nombre': 'Juan',
    'edad': 30,
    'ciudad': 'Madrid'
}

# Acceder a valores mediante claves
print(mi_diccionario['nombre'])  # Salida: 'Juan'
print(mi_diccionario['edad'])  # Salida: 30

# Modificar valores en un diccionario
mi_diccionario['edad'] = 31

# Agregar nuevos pares clave-valor a un diccionario
mi_diccionario['profesion'] = 'Ingeniero'

# Eliminar pares clave-valor de un diccionario
del mi_diccionario['ciudad']

# Verificar si una clave existe en un diccionario
if 'nombre' in mi_diccionario:
    print('La clave "nombre" existe en el diccionario')

# Obtener todas las claves de un diccionario
claves = mi_diccionario.keys()

# Obtener todos los valores de un diccionario
valores = mi_diccionario.values()

# Obtener pares clave-valor de un diccionario
items = mi_diccionario.items()

# Iterar sobre un diccionario
for clave, valor in mi_diccionario.items():
    print(clave, valor)

# Longitud de un diccionario
print(len(mi_diccionario))  # Salida: 3
