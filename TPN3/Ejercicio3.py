# Ejercicio 3: Introducir una cadena de caracteres e indicar si es un palíndromo. 
# Una palabra palíndroma es aquella que se lee igual de izquierda a derecha y de derecha a izquierda.

palabra = input('Ingresar palabra: ')
palabra = palabra.lower()
palindromo = palabra[::-1]
if palabra == palindromo:
    print(f'La palabra {palabra} es palindromo')
else:
    print(f'La palabra {palabra} no es palindromo')