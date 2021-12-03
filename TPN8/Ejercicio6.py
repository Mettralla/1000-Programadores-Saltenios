# Ejercicio 6: A partir de varios objetos de tipo diccionario genere un archivo
# JSON. En los objetos de tipo diccionario, deberá agregar los datos de tres
# clientes entre los que se encuentra el nombre, apellido, la edad y la cantidad
# gastada por cada uno.

import json

diccionarios = [
    {'Nombre': 'Daniel', 'Apellido': 'Tejerina', 'Edad': '28', 'Cantidad': '5000'},
    {'Nombre': 'Jose', 'Apellido': 'Wayar', 'Edad': '24', 'Cantidad': '4200'},
    {'Nombre': 'Julian', 'Apellido': 'Paz', 'Edad': '30', 'Cantidad': '2100'}
]

with open('TPN8/archivos/clientes.json', 'w') as archivo:
    json.dump(diccionarios, archivo, indent=4)