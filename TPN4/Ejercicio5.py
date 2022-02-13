# Ejercicio 5: Definir una función que genere una cantidad finita de cadenas con
# números enteros que puedan servir como contraseñas, las cadenas tendrán
# una longitud definida. La longitud de la cadena será un valor pasado por
# defecto en 8.

import random

def longPass():
    longdefecto = 8
    long = ''
    mensaje = int(input('''
¿Desea una contraseña de una longitud distinta a la longitud por defecto (8)?
• Si : Ingrese 1
• No : Ingrese 0
Respuesta: '''))
    if mensaje == 1:
        long = int(input('Ingresar nueva longitud: '))
    else:
        long = longdefecto
    return long

def generarpass(long):
    clave = ''
    for _ in range(long):
        clave += str(random.randint(1, long))
    return clave

long = longPass()
cantidad = int(input('Ingresar cantidad de claves a generar: '))
claves = []
for _ in range(cantidad):
    clave = generarpass(long)
    claves.append(clave)
print(claves)