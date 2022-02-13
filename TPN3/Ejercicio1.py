# Ejercicio 1: Dados N números reales indicar cuántos positivos hay en la lista.

numLista = [3, -5, 11, 3.8, 6, -2.1, -70]
contadorPositivo = 0
for num in numLista:
    if num > 0:
        contadorPositivo += 1
print(f'Hay {contadorPositivo} positivos en la lista.')