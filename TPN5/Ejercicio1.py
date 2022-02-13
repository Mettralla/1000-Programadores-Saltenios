# Ejercicio 1: Escribir una función que solicite una cadena de texto al usuario e
# indique cuántas letras mayúsculas tiene.
#
def detector_mayuscula():
    cadena = input('Ingresar texto a analizar: ')
    contador = 0
    for letra in cadena:
        if ' ' != letra == letra.upper():
            contador += 1
    return contador

contador = detector_mayuscula()
print(f'Mayusculas = {contador}')