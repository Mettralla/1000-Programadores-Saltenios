# Ejercicio 1: Crear una tabla “Productos” que contenga los datos que le permite
# a un bazar llevar el control de los productos que comercializa.
# ● Productos (id_producto, nombre_producto, cantidad_producto,
# precio_producto, categoria_producto).
# Con el código de conexión siguiente, realiza la creación de la tabla en la base de
# datos "Productos_bd".

import sqlite3

def crear_db():
    db = sqlite3.connect('TPN9/productos.db')
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos 
            (id_producto INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre_producto VARCHAR(50) NOT NULL, 
            cantidad_producto INTEGER NOT NULL, 
            precio_producto INTEGER NOT NULL, 
            categoria_producto VARCHAR(50) NOT NULL)''')
    
    db.commit()
    db.close()

crear_db()
