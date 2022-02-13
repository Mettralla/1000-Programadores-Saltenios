# Ejercicio 6: Crear una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del
# rectángulo (los puntos se formarán con una lista de 2 elementos).

# ● Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el
# origen por defecto.

# ● Añade al rectángulo un método llamado base que muestre la base.

# ● Añade al rectángulo un método llamado altura que muestre la altura.

# ● Añade al rectángulo un método llamado área que muestre el área.

class Rectangulo:

    def __init__(self, punto_inicial, punto_final):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return self.punto_final[0] - self.punto_inicial[0]

    def altura(self):
        return self.punto_final[1] - self.punto_inicial[1]

    def area(self):
        return self.base() * self.altura()

rectangulo = Rectangulo([1, 1], [3,2])
print(f'•Base de Rectangulo: {rectangulo.area()} • Altura de rectangulo: {rectangulo.altura()} • Area de Rectangulo: {rectangulo.area()}')