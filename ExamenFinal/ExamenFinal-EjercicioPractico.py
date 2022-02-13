# Diseñe una función que retorne un diccionario con la frecuencia de las VOCALES MINÚSCULAS de una cadena de texto.
# Solo se deben contar las vocales minúsculas, no los espacios en blanco, números, signos de puntuación, tampoco las
# vocales mayúsculas ni las consonantes. No se considerarán las vocales acentuadas.

# Diseñe un programa que pida el ingreso de 2 cadenas de texto, invoque adecuadamente a la función anterior y muestre
# el diccionario que posea la vocal minúscula con la mayor frecuencia de ambas colecciones, si no hay una mayor
# frecuencia indíquelo con un mensaje.

# Por ejemplo:
# contar_letras("Tres TristeS Tigres") retorna dic1={'e': 3, 'i': 2}
# contar_letras("Mi MAmá mE mima") retorna dic2={'i': 2, 'a': 1}
# La salida del programa es {'e': 3, 'i': 2}

def contar_vocales(texto):
    vocales = {
        'a': 0,
        'e': 0,
        'o': 0,
        'i': 0,
        'u': 0
    }
    lista_de_letras = []
    texto_limpio = texto.replace(' ', '')
    for letra in texto_limpio:
        lista_de_letras.append(letra)
    for letra in lista_de_letras:
        if letra == 'a':
            vocales['a'] += 1
        elif letra == 'e':
            vocales['e'] += 1
        elif letra == 'i':
            vocales['i'] += 1
        elif letra == 'o':
            vocales['o'] += 1
        elif letra == 'u':
            vocales['u'] += 1
        else:
            pass
    return vocales


def mayor_cantidad():
    cadena1 = input('Ingresar la primera cadena de texto: ')
    cadena2 = input('Ingresar la segunda cadena de texto: ')
    dic1 = contar_vocales(cadena1)
    dic2 = contar_vocales(cadena2)
    vocal_max1 = max(dic1.keys(), key=lambda k: dic1[k])
    vocal_max2 = max(dic2.keys(), key=lambda k: dic2[k])
    if dic1[vocal_max1] > dic2[vocal_max2]:
        print(
            f'La cadena con la frecuencia mas altas es: {dic1} con {dic1[vocal_max1]} vocales {vocal_max1}')
    elif dic1[vocal_max1] < dic2[vocal_max2]:
        print(dic2)
        print(
            f'La cadena con la frecuencia mas altas es: {dic2} con {dic2[vocal_max2]} vocales {vocal_max2}')
    elif dic1[vocal_max1] == dic2[vocal_max2]:
        print('Ambos diccionario comparten el mismo maximo de vocales')


mayor_cantidad()





