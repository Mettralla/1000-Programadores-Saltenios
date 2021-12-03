# Ejercicio 2: Crear un programa que lea una lista de personas, cuyos datos son
# DNI, Apellido y Nombre contenidos en un archivo csv, los liste en orden
# alfabético y muestre el resultado del ordenamiento.

import csv

lista_personas = [
    ('Apellido', 'Nombre', 'DNI'),
    ('Tejerina', 'Daniel', '1546987451'),
    ('Barrionuevo', 'Delfina', '987456321'),
    ('Tejada', 'Facundo', '6458796115'),
    ('Diaz', 'Rocio', '5489712564')
]

def crear_csv():
    with open('TPN8/archivos/lista_personas.csv', 'w', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for persona in lista_personas:
            writer.writerow(persona)

def leer_csv():
    with open('TPN8/archivos/lista_personas.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for apellido, nombre, dni in reader:
            print(apellido, nombre, dni)

def obtener_personas_csv():
    with open('TPN8/archivos/lista_personas.csv', newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        personas = []
        for persona in reader:
            personas.append(persona)
        return personas

def ordenar(lista):
    lista = sorted(lista)
    for persona in lista:
        print(persona)


leer_csv()