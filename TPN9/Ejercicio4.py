# Ejercicio 4: Crear un pequeño programa que te permita hacer una venta usando
# las tablas Productos y Detalle_Venta, considerar:
# ● Stock distinto de 0 al hacer la venta.
# ● Guardar en Detalle_Venta la venta realizada.

import sqlite3

def acceder_db():
    db = sqlite3.connect('TPN9/productos.db')
    return db

def ver_productos():
    db = acceder_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    print('Productos:'.center(50, '-'))
    for producto in productos:
        print(producto)
    print(''.center(50, '-'))
    db.close()

def comprar():
    db = acceder_db()
    cursor = db.cursor()
    id_producto = int(input('Ingresar ID del producto: '))
    cursor.execute(f'SELECT * FROM productos WHERE id_producto={id_producto}')
    producto = cursor.fetchone()
    stock = int(input('Ingresar stock a comprar: '))
    if stock <= producto[2]:
        cursor.executemany('INSERT INTO detalle_venta VALUES (?, ?, ?, ?)', [
            (id_producto, producto[3], stock, producto[3]*stock)
        ])
        db.commit()
        nuevo_stock = producto[2] - stock
        cursor.execute(f'UPDATE productos SET cantidad_producto={nuevo_stock} WHERE id_producto={id_producto}')
        db.commit()
        print('Compra realizada con exito')
        db.close()
    else:
        print('El stock que desea adquirir supera las reservas del producto')



def menu():
    print('Panel de punto de venta:'.center(50, '-'))
    print('''
    1 : Ver productos
    2 : Realizar compra
    3 : Salir
    ''')

    while True:
        opcion = int(input('Ingresar opcion deseada: '))
        if opcion == 1:
            ver_productos()
        elif opcion == 2:
            comprar()
        elif opcion == 3:
            break
        else:
            print('Ingrese opcion valida')


menu()
