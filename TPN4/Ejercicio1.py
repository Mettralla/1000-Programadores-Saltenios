# Ejercicio 1: Definir una función que calcule la suma y multiplicación de los
# elementos de una lista.

def crearLista():
    numeros = []
    n = int(input('Ingresar cantidad de numeros a operar: '))
    for i in range(n):
        numeros.append(int(input('Ingresar numero: ')))
    return numeros

def sumaLista(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

def productoLista(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


numeros = (crearLista())
print(f'''
El resultado de los numeros ingresados es:
Suma: {sumaLista(numeros)}
Multiplicacion: {productoLista(numeros)}''')