# El indexing es la forma de acceder a los elementos de una lista

lista = ['a' , 'b' , 'c' ,'d' , 'e ' , 'f' ,'g' , 'h', 'i']  

lista[0]="hello" #con esto podemo modificar el elemento de la lista selecciondo

print(lista[0])  # Esto nos mostrara el primer elemento de la lista

#print(lista[-9) tambien con un numero negativo se puede acceder aun elemento de la lista en este caso al primer elemento  

# El slicing
# el slice nos regresara una lista aunque esta tenga solo un elemento

print("Ejemplo")

print(lista[0:1])

#para ver las letras b hasta la e simplemente es:

print(lista[1:5])

# Si quiero tener por cada dos pasos una lista de elementos solo ha esto
print(lista[2:6:2])


print("# Reglas de slicing \n  1 - Un slice regresa una lista , por lo tanto, la asignacion de valores en un slice requiere una lista ")

# Ejemplo

print(lista[5:6])