# Ejercicio 1: Crear una clase llamada Persona con los atributos: nombre, edad y DNI. Diseñar los siguientes
# métodos para la clase:

# ● Un constructor, donde los datos pueden estar vacíos; ● Mostrar los datos de las personas;

# ● Determinar si es mayor de edad.


class Persona:
    def __init__(self, nombre=None, edad=None, dni=None): #Constructor
        self.nombre = nombre # Atributos de instancia
        self.edad = edad
        self.dni = dni

    def mostrar_datos(self): #Metodo
        print(f'• Nombre: {self.nombre} • Edad: {self.edad} • Dni: {self.dni}')

    def mayor_edad(self):
        if self.edad != None:
            if self.edad > 18:
                print(f'{self.nombre} es mayor de edad')
            else:
                print(f'{self.nombre} es menor de edad')
        else:
            print('Edad no ingresada')

persona1 = Persona('Daniel', 28, 123456789)
persona2 = Persona()
persona1.mostrar_datos()
persona1.mayor_edad()
persona2.mostrar_datos()
persona2.mayor_edad()