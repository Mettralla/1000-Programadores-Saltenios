# Ejercicio 3: Para la misma base de datos de ejercicios anteriores, crear una
# tabla que se llame Detalle_Venta, que contenga los siguientes campos:
# id_producto, precio_producto, cantidad, subtotal y total, de forma que permita
# armar el detalle de una factura y mostrar en pantalla.
# ● Crear la tabla Detalle_Venta.
# ● Insertar datos simulados en la tabla Detalle_Venta.

import sqlite3

def acceder_db():
    db = sqlite3.connect('TPN9/productos.db')
    return db

def crear_tabla():
    db = acceder_db()
    cursor = db.cursor()
    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS detalle_venta (
            id_producto INTEGER NOT NULL, 
            precio_producto INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,  
            subtotal INTEGER NOT NULL
            )'''
            )
    db.commit()
    db.close()

def agregar_productos():
    datos = [
        (1, 150, 1, 150*1),
        (2, 70, 10, 70*10)
    ]
    db = acceder_db()
    cursor = db.cursor()
    cursor.executemany("INSERT INTO detalle_venta VALUES (?, ?, ?, ?)", datos)
    db.commit()
    db.close()

def obtener_total():
    db = acceder_db()
    cursor = db.cursor()
    cursor.execute(
        'SELECT SUM(subtotal) FROM detalle_venta'
    )
    total = cursor.fetchone()
    print(f'Total: {total[0]}')
    db.close()



