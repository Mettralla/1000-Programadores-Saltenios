# Ejercicio 5: Escribir una clase en python que encuentre un par de elementos de una matriz dada cuya suma es igual
# a un número determinado.Se debe indicar la posición de los números que cumplen la condición.

# Entrada: números = [10,20,10,40,50,60,70], objetivo=50
# Salida: 3, 4

class Matriz:

    def __init__(self, numeros, objetivo):
        self.numeros = numeros
        self.objetivo = objetivo

    def conseguir_pares(self):
        pares = []
        for pivot in range(0, len(self.numeros)-1):
            for contenido in range(1, len(self.numeros)):
                resultado = self.numeros[pivot] + self.numeros[contenido]
                if resultado == self.objetivo:
                    pares.append([pivot,contenido])
                    break
        return pares

matriz = Matriz([10,20,10,40,50,60,70], 50)
print(matriz.conseguir_pares())