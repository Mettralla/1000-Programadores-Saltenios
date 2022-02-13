# Ejercicio 4: Escribir una clase con el nombre Monedas. Esta debe contener valores en varias monedas, por ejemplo,
# "EUR", "USD", "ARG", "YEN". Una instancia debe contener la cantidad y la unidad monetaria. La clase, que va a
# diseñar debe tener los siguientes métodos:

# ● Crear constructor

# ● Sumar distintas monedas

# ● Sumar una moneda con otro valor distinto

# ● Redefinir función _str_()

class Moneda:

    def __init__(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return self.unidad

    def convertir(self, cantidad, unidad):
        return cantidad * self.valores[unidad]

    def __add__(self, valor):
        return self.cantidad + valor

class PesoArgentino(Moneda):
    unidad = 'ARS'
    valores = {
        'EUR': 0.0088,
        'USD': 0.0100,
        'YEN': 1.14}

class Euro(Moneda):
    unidad = 'EUR'
    valores = {
        'ARS': 114.19,
        'USD': 1.14,
        'YEN': 129.92
    }

class Dolar(Moneda):
    unidad = 'USD'
    valores = {
        'ARS': 100.41,
        'EUR': 0.88,
        'YEN': 114.2
    }

class Yen(Moneda):
    unidad = 'YEN'
    valores = {
        'ARS': 0.88,
        'USD': 0.0088,
        'EUR': 0.0077
    }

ars = PesoArgentino(700)
yen = Yen(700)
suma = f"{ars.cantidad} pesos + {yen.cantidad} yenes = {ars.cantidad + yen.convertir(yen.cantidad, 'ARS')}"
print(suma)