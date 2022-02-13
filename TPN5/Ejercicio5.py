# Ejercicio 5: Escribir la función parrafos(), la cual debe generar un texto que
# contenga la cantidad de párrafos que especifique el usuario. Deberá generar las
# palabras aleatoriamente.

from faker import Faker

f = Faker()

def parrafos():
    print(f.paragraph())

cantidad = int(input('Ingresar cantidad de parrafos: '))
for _ in range(cantidad):
    parrafos()