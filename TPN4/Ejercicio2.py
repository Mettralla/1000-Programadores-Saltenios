# Ejercicio 2: Escribir una función que reciba una lista de números y un exponente
# y devuelva otra lista donde sus elementos correspondan a la lista original
# elevados al exponente dado.

def crearLista():
    numeros = []
    n = int(input('Ingresar cantidad de numeros a operar: '))
    for i in range(n):
        numeros.append(int(input('Ingresar numero: ')))
    return numeros

def operarLista(numeros):
    exponente = int(input('Ingresar exponente: '))
    listaElevada = []
    for numero in numeros:
        numeroElevado = numero ** exponente
        listaElevada.append(numeroElevado)
    return listaElevada

numeros = crearLista()
numerosExp = (operarLista(numeros))

print(f'''
Usted ha ingresado la siguiente lista: {numeros}
La potenciación de dicha lista es: {numerosExp}''')