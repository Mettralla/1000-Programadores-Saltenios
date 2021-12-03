# Escribir un programa que lea los datos de un fichero de texto, y
# transforme cada fila en un diccionario usando sus campos. Al contenido del
# diccionario añadirlo a una lista llamada personas. Luego hacer una función que
# muestre el contenido.
# El fichero de texto se denominará personas.csv y tendrá el siguiente contenido
# en texto plano(créalo previamente):
# 1, Carlos, Pérez, 05/01/1989
# 2, Manuel, Heredia, 26/12/1973
# 3, Rosa, Campos, 12/06/1961
# 4, David García, 25/07/2006
# Los campos del diccionario seguirán el orden: id, nombre, apellido y nacimiento.

import csv

def leer_como_diccionario(nombre):
    with open(nombre, 'r') as archivo:
        reader = csv.DictReader(archivo)
        for linea in reader:
            print(dict(linea))


leer_como_diccionario('TPN8/archivos/personas.csv')
