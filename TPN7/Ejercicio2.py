# Ejercicio 2: Usando la clase Personas del ejercicio nro 1 del práctico anterior, crear 2 clases, Alumnos y Profesores.
# Asignar notas a los alumnos de acuerdo a las siguientes materias (lengua, matemática, historia, geografía) y una
# comisión (A, B, C) de acuerdo al promedio de sus notas (A si es >=8, B si es >=6 y <8, C si es <6). A los Profesores
# asignar como máximo 1 materia.

# ● Los datos personales de alumnos y profesores no pueden ser nulos

# ● Asignar comisión al alumno. No se puede tener acceso de forma directa al atributo comisión. Si el alumno es mayor
# de 17 asignar a una comisión especial N

# ● Mostrar todas las notas identificando a qué materia pertenece

# ● Los profesores pueden evaluar y asignar notas a los alumnos.

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar_datos(self):
        print(f'• Nombre: {self.nombre} • Edad: {self.edad} • Dni: {self.dni}')

    def mayor_edad(self):
        if self.edad > 18:
            print(f'{self.nombre} es mayor de edad')
        else:
            print(f'{self.nombre} es menor de edad')


class Alumno(Persona):

    materias = ['Lengua', 'Matematica', 'Historia', 'Geografia']
    diccionario_materias = {}

    def __asignar_comision(self, notas_materias):
        promedio = sum(notas_materias) // len(notas_materias)
        if promedio >= 8:
            self.__comision = 'A'
        elif promedio >= 6:
            self.__comision = 'B'
        else:
            self.__comision = 'C'

    def __asignar_notas(self, notas_materias):
        for posicion, materia in enumerate(self.materias):
            self.diccionario_materias[materia] = notas_materias[posicion]

    def __init__(self, nombre, edad, dni, notas_materias):
        Persona.__init__(self, nombre, edad, dni)
        self.notas_materias = notas_materias
        self.__asignar_notas(notas_materias)
        if edad > 17:
            self.__comision = 'N'
        else:
            self.__asignar_comision(notas_materias)

    def mostrar_comision(self):
        return f'El alumno {self.nombre} pertence a la comision: {self.__comision}'

    def mostrar_notas(self):
        for materia, nota in self.diccionario_materias.items():
            print(f'Materia: {materia} - Nota: {nota}')


class Profesor(Persona):

    def __init__(self, nombre, edad, dni, materia):
        Persona.__init__(self, nombre, edad, dni)
        self.materia = materia

    def asignar_nota(self, alumno, nota_nueva):
        alumno.diccionario_materias[self.materia] = nota_nueva
        print(f'La nueva nota del {alumno1.nombre} en la materia {self.materia} es: {alumno1.diccionario_materias[self.materia]} ')


alumno1 = Alumno('Daniel', 15, 123456789, [8, 5, 6, 9])

profesor1 = Profesor('Juan', 35, 154897412, 'Lengua')

profesor1.asignar_nota(alumno1, 7)

alumno1.mostrar_notas()
