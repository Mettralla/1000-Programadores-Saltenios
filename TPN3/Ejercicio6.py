# Ejercicio 6: Una local de comida rápida ('ML') conocido de la ciudad ofrece hamburguesas vegetarianas y no
# vegetarianas a sus clientes. Los ingredientes para cada tipo aparecen a continuación:

# ● Ingredientes vegetarianos: calabaza - soja
# ● Ingredientes no vegetarianos: carne vacuna - carne de pollo

# Escribir un programa que pregunte al usuario si quiere una hamburguesa vegetariana o no, y en función de su
# respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente
# además de la lechuga, queso y el tomate que están en todas las hamburguesas. Al final se debe mostrar por pantalla
# si la hamburguesa elegida es vegetariana o no y todos los ingredientes que lleva.

ingVegetariano = ['Calabaza', 'Soja']
ingNovegetariano = ['Carne Vacuna', 'Carne de Pollo']
hamburguesa = int(input(
    'Ingresar 1 para hamburguesa vegetariana o 2 para hamburguesa no vegetariana: '))
ordenCliente = ['Lechuga', 'Queso', 'Tomate']
tipo = 'None'
if hamburguesa == 1:
    print(f'''Los ingredientes vegetarianos son: 
    1- {ingVegetariano[0]}
    2- {ingVegetariano[1]}''')
    opcionVeg = int(input("Ingresar numero para escoger ingrediente: "))
    if opcionVeg == 1:
        ordenCliente.append(ingVegetariano[0])
    elif opcionVeg == 2:
        ordenCliente.append(ingVegetariano[1])
    tipo = 'Vegetariana'
elif hamburguesa == 2:
    print(f'''Los ingredientes no vegetarianos son: 
    1- {ingNovegetariano[0]}
    2- {ingNovegetariano[1]}''')
    opcionNoveg = int(input("Ingresar numero para escoger ingrediente: "))
    if opcionNoveg == 1:
        ordenCliente.append(ingNovegetariano[0])
    elif opcionNoveg == 2:
        ordenCliente.append(ingNovegetariano[1])
    tipo = 'No Vegetariana'
print(f'''Ha ordenado una hamburguesa {tipo}, los ingredientes son:
    • {ordenCliente[0]}
    • {ordenCliente[1]}
    • {ordenCliente[2]}
    • {ordenCliente[3]}''')
