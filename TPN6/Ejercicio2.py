# Ejercicio 2: Crear una clase llamada Cuenta que tendrá los atributos: titular (que es una persona) y
# cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los
# siguientes métodos para la clase:

# ● Un constructor;
# ● El atributo cuenta no se puede modificar directamente, sólo ingresando o retirando dinero;
# ● mostrar(): Muestra los datos de la cuenta;
# ● ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada;
# ● retirar(cantidad): se retira

class Cuenta:

    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.__cantidad = cantidad

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


cuenta1 = Cuenta('Daniel Tejerina', cantidad=1000)
cuenta1.mostrar_cuenta()
cuenta1.ingresar(500)
cuenta1.retirar(700)
cuenta1.mostrar_cuenta()