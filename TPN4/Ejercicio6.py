# Ejercicio 6: Definir una función que concatena las cadenas que se reciba como
# parámetros no importa la cantidad de los mismos, de forma que devuelva una
# oración.

def crearOracion():
    palabras = []
    n = int(input('Ingresar cantidad de palabras: '))
    for i in range(n):
        palabras.append(input('Ingresar palabra: '))
    return ' '.join(palabras)

oracion = crearOracion()
print(f'La oracion es: {oracion}')