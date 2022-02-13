# Ejercicio 5: Crear una clase con los datos de una cuenta de correo electrónico. Cada dato de la cuenta de correo
# (id, dominio, y password) debe digitarse por separado.

# Al mostrar la cuenta los datos de ID y dominio deben aparecer unidos. Por ejemplo: juan@gmail.com. Debe validarse el
# password, solicitando que sea digitado dos veces.

# ● Crear constructor usando input() y getpass()

# ● El password no se puede editar directamente, se debe crear una función específica para tal operación

# ● Mostrar dirección de mail

from getpass import getpass

base_de_datos = {'daniel@gmail.com': 'trustno1'}

class Usuario:

    def __init__(self, id, dominio, password):
        self.correo = id + '@' + dominio
        if base_de_datos[self.correo] == password:
            print('Bienvenido')
        else:
            print('Contrasena Incorrrecta')

id = input('Ingresa tu ID del correo: ')
dominio = input('Ingresa el dominio SIN el @: ')
password = getpass(prompt='Ingresa la contrasena: ')

usuario = Usuario(id, dominio, password)