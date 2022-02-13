# Ejercicio 2: Escribir un algoritmo que almacene una cadena de texto que contenga una contraseña cualquiera.
# Luego debe ofrecer 3 intentos para el ingreso de una nueva cadena de texto. Cuando las contraseñas coincidan
# ya no se deberá solicitar más ingresos y se mostrará un mensaje diciendo “FELICITACIONES”. Además deberá
# mostrar un mensaje advirtiendo “CONTRASEÑA BLOQUEADA” si falló todos los intentos. Piensa bien en la condición
# o valores que pueden indicar esa situación.

password = ('trustno1')
contadorIntentos = 0
while contadorIntentos < 3:
    login = input('Ingresar password: ')
    if login == password:
        print('¡Felicitaciones!')
        contadorIntentos = 4
    else:
        print('¡Contraseña incorrecta!')
        contadorIntentos += 1
if contadorIntentos == 3:
    print('¡Contraseña bloqueada!')