# Ejercicio 3: Diseñar una clase Cuentas Bancarias que tiene como atributo una Lista de cuentas.
# Añadir las siguientes funcionalidades:

# ● Crear constructor;
# ● Saldo_deudor: Muestra el saldo deudor total de todas las cuentas con saldo negativo;
# ● Mostrar todas las cuentas con saldo negativo con el valor adeudado.

class Cuenta:

    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

    def __repr__(self):
        return f'<Cuenta: {self.titular}>'

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nuevo_valor):
        print('No se puede modificar directamente, usar el metodo ingresar()')

    def mostrar_cuenta(self):
        print(f'• Titular: {self.titular} • Cantidad: {self.__cantidad}')

    def ingresar(self, deposito):
        if deposito > 0:
            self.__cantidad += deposito
            print(f'Usted ha depositado ${deposito}, el monto total de su cuenta es: ${self.__cantidad}')
        else:
            print('Solo puede ingresar valor mayores que 0')

    def retirar(self, retiro):
        if retiro > 0:
            self.__cantidad -= retiro
            print(f'Usted ha retirado ${retiro}, el monto total de su cuenta es: ${self.__cantidad}')
        else:
            print('Solo puede retirar valor mayores que 0')

    def saldo(self):
            return self.__cantidad

class Banco:

    lista_cuentas = []

    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_cuenta(self, cuenta):
        self.lista_cuentas.append(cuenta)

    def saldo_deudor(self):
        if self.lista_cuentas:
            for cuenta in self.lista_cuentas:
                cantidad = cuenta.saldo()
                if cantidad < 0:
                    print(f'La cuenta de {cuenta.titular} tiene un saldo negativo: {cantidad}')
        else:
            print('No hay cuentas asignadas a este banco')

banco1 = Banco('Banco Brubank')

cuenta1 = Cuenta('Daniel', -500)
cuenta2 = Cuenta('Lucas', -1500)
cuenta3 = Cuenta('Pamela', 4500)

banco1.agregar_cuenta(cuenta1)
banco1.agregar_cuenta(cuenta2)
banco1.agregar_cuenta(cuenta3)

banco1.saldo_deudor()