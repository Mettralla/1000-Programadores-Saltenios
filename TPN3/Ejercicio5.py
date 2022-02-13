# Ejercicio 5: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior
# a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre
# por pantalla el grupo que le corresponde.

nombreAnt = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' 'l' 'm']
nombrePos = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' 'y' 'z']
mujer = ['mujer', 'm']
hombre = ['hombre', 'h']
nombre = input('Ingresar nombre: ')
nombre = nombre.lower()
sexo = input('Ingresar sexo (Mujer/Hombre): ')
sexo = sexo.lower()
if nombre[0] in nombreAnt and sexo in mujer:
    print('Pertenece al Grupo A')
elif nombre[0] in nombrePos and sexo in hombre:
    print('Pertenece al Grupo A')
else:
    print('Pertenece al Grupo B')