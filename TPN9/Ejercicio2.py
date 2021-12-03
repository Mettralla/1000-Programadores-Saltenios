# Ejercicio 2: Una vez creada la base de datos "Productos_bd" y la tabla
# "Productos" realice las siguientes actividades:
# ● Insertar un producto
# ● Hacer al menos una consulta de búsqueda. Ejemplo: "ver todos los
# productos cargados", "ver los productos con stock 0"
# ● Actualizar un producto
# ● Eliminar un producto

import sqlite3

def acceder_db():
    db = sqlite3.connect('TPN9/productos.db')
    return db

def insertar_producto():
    db = acceder_db()
    cursor = db.cursor()
    nombre = input('Ingresar nombre del producto: ')
    cantidad = int(input('Ingresar cantidad del producto: '))
    precio = int(input('Ingresar precio del producto: '))
    categoria = input('Ingresar categoria del producto: ')
    datos = [(None, nombre, cantidad, precio, categoria)]
    cursor.executemany('INSERT INTO productos VALUES (?, ?, ?, ?, ?)', datos)
    db.commit()
    db.close()

def realizar_consulta():
    db = acceder_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    db.close()

def consultar_producto_agotado():
    db = acceder_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM productos WHERE cantidad_producto = 0')
    productos = cursor.fetchall()
    for producto in productos:
        print(producto)
    db.close()

def actualizar_nombre_producto():
    db = acceder_db()
    cursor = db.cursor()
    id_producto = int(input('Ingresar ID de producto: '))
    nuevo_nombre = input('Ingresar nuevo nombre: ')
    cursor.execute(f'UPDATE productos SET nombre_producto = "{nuevo_nombre}" WHERE id_producto ="{id_producto}"')
    db.commit()
    db.close()

def eliminar_producto():
    db = acceder_db()
    cursor = db.cursor()
    id_producto = int(input('Ingresar ID de producto: '))
    cursor.execute(f'DELETE FROM productos WHERE id_producto="{id_producto}"')
    db.commit()
    db.close()

def menu():
    print('Panel de consulta de la base de datos:'.center(50,'-'))
    print('''
    1 : Insertar productos
    2 : Ver productos cargados
    3 : Consultar productos agotados
    4 : Actualizar un producto
    5 : Eliminar un producto
    6 : Salir
    ''')

    while True:
        opcion = int(input('Ingresar opcion deseada: '))
        if opcion == 1:
            insertar_producto()
        elif opcion == 2:
            realizar_consulta()
        elif opcion == 3:
            consultar_producto_agotado()
        elif opcion == 4:
            actualizar_nombre_producto()
        elif opcion == 5:
            eliminar_producto()
        elif opcion == 6:
            break
        else:
            print('Opcion no encontrada - Ingrese opcion valida')


menu()

