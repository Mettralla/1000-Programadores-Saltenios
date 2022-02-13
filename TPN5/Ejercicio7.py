# Ejercicio 7: Definir una función que divida dos números, debe contemplar el uso
# de excepciones para salvar el error de dividir por cero.

def dividir (numerador, denominador):
    try:
        return numerador/denominador
    except ZeroDivisionError:
        print('No se puede dividir por cero')

numerador = int(input('Ingresar numerador: '))
denominador = int(input('Ingresar denominador: '))

resultado = dividir(numerador, denominador)

if resultado is None:
    print(f'El resultado es: {resultado}')