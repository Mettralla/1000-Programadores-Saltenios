# Ejercicio 3: Crear una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del
# rectángulo (los puntos se formarán con una lista de 2 elementos). Usar la clase punto como superclase.

# ● Añadir un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el
# origen por defecto.

# ● Añadir al rectángulo un método llamado base que muestre la base.

# ● Añadir al rectángulo un método llamado altura que muestre la altura.

# ● Añadir al rectángulo un método llamado área que muestre el área.

# ● Dibujar el rectángulo, usar "matplotlib".

import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Punto:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def __str__(self):
        return f'{self.__x},{self.__y}'

    def __repr__(self):
        return (self.__x, self.__y)


    def cuadrante(self):
        if self.__x > 0 and self.__y > 0:
            return 'Pertenece al cuadrante 1'
        elif self.__x < 0 and self.__y > 0:
            return 'Pertenece al cuadrante 2'
        elif self.__x < 0 and self.__y < 0:
            return 'Pertenece al cuadrante 3'
        elif self.__x > 0 and self.__y < 0:
            return 'Pertenece al cuadrante 4'
        elif self.__x == 0 and self.__y != 0:
            return 'Pertenece al eje Y'
        elif self.__x != 0 and self.__y == 0:
            return 'Pertenece al eje X'
        elif self.__x == 0 and self.__y == 0:
            return 'Esta en el origen'

    def vector(self, vector): # vector = extremo - origen
        primero = vector[0] - self.__x
        segundo = vector[1] - self.__y
        return [primero, segundo]


class Rectangulo():

    def __init__(self, punto_inicial=None, punto_final=None):
        if punto_inicial == None:
            self.punto_inicial = Punto()
        else:
            self.punto_inicial = punto_inicial
        if punto_final == None:
            self.punto_final = Punto()
        else:
            self.punto_final = punto_final

    def __str__(self):
        return f'{self.__x},{self.__y}'

    def base(self):
        return self.punto_final[0] - self.punto_inicial[0]

    def altura(self):
        return self.punto_final[1] - self.punto_inicial[1]

    def area(self):
        return self.base() * self.altura()

    def show(self):
        fig,ax = plt.subplots()
        ax.plot([1,4], [1,4])
        ax.add_patch(
            patches.Rectangle(
                (self.punto_inicial),
                self.base(),
                self.altura(),
                edgecolor='blue',
                facecolor='red',
                fill=True
            ))
        plt.show()

punto_inicial = (1, 1)
punto_final = (3, 2)

rectangulo = Rectangulo(punto_inicial, punto_final)

print(f'•Base de Rectangulo: {rectangulo.area()} • Altura de rectangulo: {rectangulo.altura()} • Area de Rectangulo: {rectangulo.area()}')
rectangulo.show()