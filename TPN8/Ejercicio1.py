# Ejercicio 1: Crear las siguientes funciones (el archivo estará en tu google drive):
# ● Crear archivo de texto
# ● Abrir y mostrar contenido de archivo de texto
# ● Guardar datos en archivo de texto.

from io import open
from os import read

#crear archivo

def crear_fichero(texto):
    fichero = open('fichero.txt', "w")
    fichero.write(texto)
    fichero.close()

#mostrar archivo

def mostrar_fichero():
    fichero = open('fichero.txt', "r")
    texto = fichero.read()
    fichero.close()
    print(texto)

#Guardar archivos

def agregar_datos(nueva_linea):
    fichero = open('fichero.txt', 'a')
    fichero.write(nueva_linea)
    fichero.close()


texto = 'Primera linea de texto\nsegunda linea de texto\ntercera linea de texto\ncuarta linea de texto\nquinta linea de texto.\n'

crear_fichero(texto)
mostrar_fichero()
agregar_datos('Sexta linea de texto.\n')
mostrar_fichero()