# Ejercicio 7: Definir una función que reciba un diccionario que contenga nombre
# completo y correo electrónico de una lista de personas, la cantidad de personas
# puede variar y debe mostrarse de forma ordenada.

def crearDiccionario(nombresLista, correosLista):
    diccionario = {}
    for posicion in range(0, len(nombresLista)):
        nombre = nombresLista[posicion]
        correo = correosLista[posicion]
        diccionario[nombre] = correo
    return diccionario

nombresLista = ["Caceres", "Gomez", "Lamas"]
correosLista = ["Pedro@gmail.com", "Manaza@hotmail.com", "Pera@yahoo.com"]
diccionario = crearDiccionario(nombresLista, correosLista)

print(diccionario)
