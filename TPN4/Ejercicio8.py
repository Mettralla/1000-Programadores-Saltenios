# Ejercicio 8: Definir una función que reciba un parámetro por referencia y otra
# que sea un parámetro por valor.

#Paso por valor

def pasoValor(numero):
    print(f'Valor inicial: {numero}')
    numero += 5
    print(f'Valor modificado: {numero}')

#Paso Referencia

def pasoReferencia(lista):
    print(f'Valor inicial: {lista}')
    for i in range(len(lista)):
        lista[i] *= 2
    print(f'Valor modificado: {lista}')

#Llamadas

print('• Paso por Valor:')
numero = 10
pasoValor(numero)
print(f'Valor Original: {numero}')

print('• Paso Referencia:')
lista = [4, 5, 6, 10]
pasoReferencia(lista)
print(f'Valor original: {lista}')