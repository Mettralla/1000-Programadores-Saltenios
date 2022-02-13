# Ejercicio 8: Crear una clase Fecha con atributos para el día, el mes y el año de la fecha. Incluye, al menos, los
# siguientes métodos:

# ● Constructor predeterminado con el 1-1-1900 como fecha por defecto.

# ● año_bisiesto(): indicará si el año de la fecha es bisiesto o no.

# ● dias_mes(int): devolverá el número de días del mes que se le indique (para el año de la fecha).

# ● validar(): comprobará si la fecha es correcta (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo
# pondrá a 1; si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900. Será un método
# auxiliar (privado).

# ● Definir métodos getter y setter.

# ● hoy(): devuelve la fecha actual.

# ● corta(): mostrará la fecha en formato corto (02-09-2003).

# ● larga(): mostrará la fecha en formato largo, empezando por el día de la semana (martes 2 de septiembre de 2003).
# los días que se indiquen desde el 1-1-1900.

class Fecha:

    def __init__(self, dia= 1, mes= 1, anio= 1900):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    def corta(self):
        print(f'{self.__dia} / {self.__mes} / {self.__anio}')

    def larga(self):
        print(f'{self.__dia} de {self.__meses[self.__mes - 1]} del {self.__anio}')

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        self.__mes = mes

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    def bisiesto(self):
        bis = None
        if self.__anio % 4 != 0:  # no divisible entre 4
            bis = False
            print("No es bisiesto")
        elif self.__anio % 4 == 0 and self.__anio % 100 != 0:  # divisible entre 4 y no entre 100 o 400
            bis = True
            print("Es bisiesto")
        elif self.__anio % 4 == 0 and self.__anio % 100 == 0 and self.__anio % 400 != 0:  # divisible entre 4 y 10 y no entre 400
            bis = False
            print("No es bisiesto")
        elif self.__anio % 4 == 0 and self.__anio % 100 == 0 and self.__anio % 400 == 0:  # divisible entre 4, 100 y 400
            bis = True
            print("Es bisiesto")
        return bis

    def reprogramar(self):
        fecha.__dia = 1
        fecha.__mes = 1
        fecha.__anio = 1900

    def __validar(self):
        meses_30 = {4, 6, 9, 11}
        meses_31 = {1, 3, 5, 7, 8, 10, 12}
        if (1900 > self.__anio or self.__anio > 2050) and isinstance(self.__anio, int):
            fecha.reprogramar()
        elif (1 > self.__mes or self.__mes > 12) and isinstance(self.__mes, int):
            fecha.reprogramar()
        elif self.__mes == 2 and (1 < self.__dia or self.__dia > 29):
            if condicion_bisiesto == True and (1 > self.__dia or self.__dia > 29):
                fecha.reprogramar()
            if condicion_bisiesto == False and (1 > self.__dia or self.__dia > 28):
                fecha.reprogramar()
        elif self.__mes in meses_31:
            if (1 > self.__dia or self.__dia > 31) and isinstance(self.__dia, int):
                fecha.reprogramar()
        elif self.__mes in meses_30:
            if (1 > self.__dia or self.__dia > 30) and isinstance(self.__dia, int):
                fecha.reprogramar()
        return (f'{self.__dia} / {self.__mes} / {self.__anio}')

    def validacion_publica(self):
        print(fecha.__validar())

    def dia_mes(self):
        meses_30 = {4, 6, 9, 11}
        meses_31 = {1, 3, 5, 7, 8, 10, 12}
        if self.__mes in meses_30:
            print(f'El mes de {self.__meses[self.__mes - 1]} tiene 30 dias')
        elif self.__mes in meses_31:
            print(f'El mes de {self.__meses[self.__mes - 1]} tiene 31 dias')
        elif self.__mes == 2 and condicion_bisiesto == True:
            print(f'El mes de {self.__meses[self.__mes - 1]} tiene 29 dias')
        elif self.__mes == 2 and condicion_bisiesto == False:
            print(f'El mes de {self.__meses[self.__mes - 1]} tiene 28 dias')


fecha = Fecha(28, 2, 2021)
condicion_bisiesto = fecha.bisiesto()
fecha.validacion_publica()
fecha.corta()
fecha.larga()
fecha.dia_mes()