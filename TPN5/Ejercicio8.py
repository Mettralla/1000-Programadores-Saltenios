# Ejercicio 8: Definir una función que devuelva el valor máximo de una lista
# indefinida de elementos. Usar algunas funciones integradas de Python

def detectar_mayor(lista: list):
    return max(lista)

lista = []
while True:
    numero = int(input('Ingresar un numero: '))
    lista.append(numero)
    opcion = input('Desea salir? S/N: ')
    if opcion.lower() == 's':
        break

maximo = detectar_mayor(lista)
print(f'El mayor es: {maximo}')