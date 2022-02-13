# Ejercicio 7: Crear una clase llamada Punto con 2 coordenadas (atributos) X e Y:

# ● Añade un método constructor para crear puntos fácilmente. Si no se recibe una coordenada, su valor será cero.

# ● Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)

# ● Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e
# Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.

# ● Añade un método llamado vector, que tome otro punto y calcule el vector (se representaría como la diferencia entre
# las coordenadas del segundo punto respecto al primero) resultante entre los dos puntos.

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return (self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 'Pertenece al cuadrante 1'
        elif self.x < 0 and self.y > 0:
            return 'Pertenece al cuadrante 2'
        elif self.x < 0 and self.y < 0:
            return 'Pertenece al cuadrante 3'
        elif self.x > 0 and self.y < 0:
            return 'Pertenece al cuadrante 4'
        elif self.x == 0 and self.y != 0:
            return 'Pertenece al eje Y'
        elif self.x != 0 and self.y == 0:
            return 'Pertenece al eje X'
        elif self.x == 0 and self.y == 0:
            return 'Esta en el origen'

    def vector(self, vector): # vector = extremo - origen
        primero = vector[0] - self.x
        segundo = vector[1] - self.y
        return [primero, segundo]

punto = Punto(3,4)
vector = (7,6)
print(punto.cuadrante())
print(punto.vector(vector))