# Ejercicio 1: Crear una clase de números enteros y redefinir las funciones
# elementales (+ , - , *, /) usando los métodos denominados mágicos.
# ● Sobrecargar el operador "/": si el divisor es 0 devuelve como resultado 0
# y un msj de error.

class NumeroEntero:

    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return str(self.numero)

    def __repr__(self):
        return f'<NumeroEntero: {self.numero}>'

    def __add__(self, sumando):
        return f'El resultado es: {self.numero + sumando}'

    def __sub__(self, sustraendo):
        return f'El resultado es: {self.numero - sustraendo}'

    def __mul__(self, multiplicador):
        return  f'El resultado es: {self.numero * multiplicador}'

    def __truediv__(self, denominador):
        if denominador != 0:
            return f'El resultado es: {self.numero / denominador}'
        else:
            print('No se puede dividir por cero')
            return f'El resultado es: {0}'

numero1 = NumeroEntero(15)
print(numero1 + 5)
print(numero1 - 5)
print(numero1 * 2)
print(numero1 / 0)