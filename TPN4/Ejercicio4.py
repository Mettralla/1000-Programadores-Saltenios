# Ejercicio 4: Definir una función llamada separar() que tome una lista de
# números enteros y devuelva dos listas ordenadas de menor a mayor: la primera
# con los números pares y la segunda con los números impares.

def crearLista():
    numeros = []
    n = int(input('Ingresar cantidad de numeros a operar: '))
    for i in range(n):
        numeros.append(int(input('Ingresar numero: ')))
    return numeros

def separar(numerosEnteros):
    listaPar = []
    listaImpar = []
    for numero in numerosEnteros:
        if numero % 2 == 0:
            listaPar.append(numero)
        else:
            listaImpar.append(numero)
    parOrdenado = sorted(listaPar)
    imparOrdenado = sorted(listaImpar)
    return parOrdenado, imparOrdenado

numerosEnteros = crearLista()
parOrdenado, imparOrdenado = separar(numerosEnteros)

print(f'''
• La lista de numeros enteros ingresados: {numerosEnteros}
• Pares ordenados de menor a mayor: {parOrdenado}
• Impares ordenados de menor a mayor: {imparOrdenado}
''')