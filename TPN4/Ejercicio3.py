# Ejercicio 3: Escribir una función que convierta un número entero expresado en base decimal
# a binario y otra función que convierta un número entero binario a base decimal.

def decimal_to_binario(numeroDecimal):
    comprobacionBinario = format(numeroDecimal, "b")
    listaModulo = []
    binario = ""
    while numeroDecimal != 0:
        modulo = numeroDecimal % 2
        listaModulo.append(modulo)
        numeroDecimal //= 2
    for numero in listaModulo:
        binario += str(numero)
    binario = binario[::-1]
    if binario == comprobacionBinario:
        print(f'El numero {binario} es binario.')
    else:
        print(f'El numero {binario} no es binario.')
    return int(binario)

def binario_to_decimal(binario):
    comprobacionDecimal = (int(binario, 2))
    exponente = 0
    binario = binario[::-1]
    decimal = 0
    for numero in binario:
        decimal += int(numero)*2**exponente
        exponente += 1
    if decimal == comprobacionDecimal:
        print(f'El numero {decimal} es decimal.')
    else:
        print(f'El numero {decimal} no es decimal.')
    return decimal

# Convertir Decimal a Binario
numeroDecimal = int(input('Ingresar numero en base decimal: '))
binarioConvertido = decimal_to_binario(numeroDecimal)
print(f'El binario de {numeroDecimal} es: {binarioConvertido}')

# Convertir Binario a Decimal
binario = input('Ingresar numero binario: ')
decimalConvertido = (binario_to_decimal(binario))
print(f'El decimal de {binario} es: {decimalConvertido}')