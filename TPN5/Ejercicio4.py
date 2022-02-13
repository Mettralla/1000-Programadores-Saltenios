# Ejercicio 4: Las reglas de cierto juego con dados son las siguientes: El jugador
# debe hacer una apuesta de dinero y elegir lanzar con 1, 2 o 3 dados. Diseñe una
# función que trabaje con cualquier cantidad de dados y retorne la suma de sus
# valores. El script debe solicitar el monto de la apuesta, preguntar al usuario con
# cuántos dados jugará, generar aleatoriamente los valores de los dados e
# invocar adecuadamente a la función. Luego decidir el resultado de la apuesta
# de la siguiente manera:

# ● Si jugó con 1 dado, el jugador gana el 10% de lo apostado si la suma fue mayor a 4.

# ● Si jugó con 2 dados, el jugador gana el 50% de lo apostado si la suma fue mayor a 8.

# ● Si jugó con 3 dados, el jugador gana el 300% de lo apostado si la suma es 18.

from random import randint

def tirada(dados):
    resultado_tirada = 0
    if 1 <= dados <= 3:
        for _ in range(dados):
            resultado_tirada += randint(1,6)
    else:
        print('Ingrese un valor del 1-3')
    return resultado_tirada

def resultado_apuesta(dados, resultado_tirada, monto_apostado):
    premio = monto_apostado
    if resultado_tirada != 0:
        if resultado_tirada > 4 and dados == 1:
            premio *= 0.1
            print(f'Su tirada fue {resultado_tirada} y ha ganado {premio}')
        elif resultado_tirada > 8 and dados == 2:
            premio *= 0.5
            print(f'Su tirada fue {resultado_tirada} y ha ganado {premio}')
        elif resultado_tirada > 18 and dados == 3:
            premio *= 3
            print(f'Su tirada fue {resultado_tirada} y ha ganado {premio}')
        else:
            print(f'Su tirada fue {resultado_tirada}, mejor suerte la proxima')
    else:
        print('Realice nuevamente la tirada')


monto_apostado = float(input('Ingresar apuesta: '))
dados = int(input('Cuantos dados desea lanzar (1-3):  '))
resultado_tirada = tirada(dados)
resultado_apuesta(dados, resultado_tirada, monto_apostado)