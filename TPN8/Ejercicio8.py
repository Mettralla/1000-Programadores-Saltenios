# Ejercicio 8: Con el archivo Entidades.json que contiene un conjunto de clases y
# sus propiedades realizar una función que lea el archivo decodificandolo.
# Ayuda:
# ● Primero debemos abrir el archivo json, indicando donde se encuentra a la
# función open(), en forma de solo lectura.
# ● Luego debemos leer el contenido con la función read(), y lo guardaremos
# en una variable contenido.
# ● Por último es necesario descodificar el JSON para que podamos
# utilizarlo posteriormente dentro de nuestra aplicación. Por lo que
# llamamos al paquete JSON para ejecutar la función loads() sobre el
# contenido leído previamente. De esa forma tendremos el contenido de
# JSON en memoria y podremos trabajar con él.

import json

with open('TPN8/archivos/Entidades.json', 'r') as archivo:
    datos = json.load(archivo)
    print(json.dumps(datos, indent=4))