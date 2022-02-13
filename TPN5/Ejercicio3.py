# Ejercicio 3: Realizar un programa que muestre al usuario una lista de productos,
# permita ingresar el código del producto elegido y la cantidad de unidades que
# desea comprar. Finalmente, el programa debe calcular el total a pagar
# simulando una factura. Diseñe todas las funciones que considere necesarias
# para el correcto funcionamiento del programa.


def mostrar_productos(productos: dict): #Muestra los productos
    print('''
Codigo   Producto
    ''')
    for codigo, producto in productos.items():
        print(f''' {codigo}     {producto[0]} - Precio: ${producto[1]}''')


def armar_carrito(productos: dict, carrito: list): #Agrega productos al carrito
    mostrar_productos(productos)
    codigo = input('Ingresar el codigo de producto deseado: ')
    if codigo.isnumeric():
        if productos.get(codigo):
            producto = productos[codigo]
            print(f'Producto seleccionado: {producto[0]} - Precio: {producto[1]}')
            cantidad = int(input('Ingrese cantidad: '))
            if cantidad > 0:
                sub_total = producto[1] * cantidad
                producto.append(sub_total)
                carrito.append(producto)
            else:
                print('La cantidad solamente es positiva')
        else:
            print('El codigo ingresado no existe')
    else:
        print('El codigo debe ser numerico')

def mostrar_carrito(carrito: list): #Muestra el contenido del carrito
    if carrito:
        for producto in carrito:
            print(f'Producto: {producto[0]} Precio Unitario: {producto[1]} Subtotal: {producto[2]}')
    else:
        print('El carrito esta vacio')

def generar_ticket(carrito: list): #Genera el ticket con el total a pagar
    mostrar_carrito(carrito)
    total = 0
    for producto in carrito:
        total += producto[2]
    print(f'Total a pagar: {total}')


productos = {
    '101': ['Aceite Girasol Cocinero 1.5 Lt', 125],
    '102': ['Aceite Girasol Natura 1.5 Lt', 146],
    '103': ['Arroz Gallo Oro 1 Kg', 98],
    '104': ['Arroz Lucchetti Largo Fino x 1 Kg', 62],
    '105': ['Fideos Lucchetti Tirabuzon 500 Gr', 52],
    '106': ['Fideos Mattarazzo Tallarin 500 Gr', 57],
    '107': ['Harina Cañuelas Trigo 000 x 1 Kg', 35],
    '108': ['Harina Blancaflor Leudante 1 Kg', 66],
    '109': ['Yerba Amanda 1 Kg', 219],
    '110': ['Yerba Taragüi 1 Kg', 228],
    '111': ['Choclo Lata Arcor Ama. Cremoso x 300 Gr', 62],
    '112': ['Picadillo Lata Swif Carne 90 Gr', 35],
    '113': ['Lavandina Querubin 1 Lt', 58],
    '114': ['Jabón en Pan Federal x 150 Gr', 47],
    '115': ['Papel Higiénico Higienol D. Hoja x 6 Un. x 180m', 183],
}

carrito = []

while True:
    print('''
    --- Super Python - Carrito de Compra ---

    Selecciona una opcion:
    1) Mostrar lista de productos
    2) Agregar producto al carrito
    3) Mostrar carrito
    4) Generar ticket
    5) Salir
    ''')
    opcion = int(input('Ingresa una opcion: '))
    if opcion:
        if opcion == 1:
            mostrar_productos(productos)
        elif opcion == 2:
            armar_carrito(productos, carrito)
        elif opcion == 3:
            mostrar_carrito(carrito)
        elif opcion == 4:
            generar_ticket(carrito)
        else:
            print('Ingrese una opcion de 1 al 4')
    else:
        print('Ingrese valores numericos')