# Ejercicio 3: Escribir un programa que acceda a un archivo de texto de google drive y muestre por pantalla el número de palabras que contiene.

from io import open
from os import read

with open('contador.txt', 'r') as archivo:
    lineas = archivo.readlines()
    print(lineas)
    contador = 0
    for palabra in lineas:
        palabras = palabra.split(' ')
        contador += len(palabras)
    print(f'La cantidad de palabras en el archivos es: {contador}')