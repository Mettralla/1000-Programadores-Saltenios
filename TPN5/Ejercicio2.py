# Ejercicio 2: Escribir un programa que pida dos o más palabras separadas por
# una coma e indique si cada par de palabras riman o no. Si coinciden las tres
# últimas letras tiene que indicar que riman. Si coinciden sólo las dos últimas
# tiene que indicar que riman un poco y si no, que no riman.

def creacion_lista():
    palabras = input('Ingrese palabras separadas por una coma: ')
    lista_palabras = palabras.split(',')
    return lista_palabras

def rima(pal_1, pal_2):
    fin_pal_1 = pal_1[-3:]
    fin_pal_2 = pal_2[-3:]
    if fin_pal_1 == fin_pal_2:
        print(f'{pal_1} rima con {pal_2}')
    elif fin_pal_1[-2:] == fin_pal_2[-2:]:
        print(f'{pal_1} rima un poco con {pal_2}')
    else: print(f'{pal_1} no rima {pal_2}')

def verif_rima(lista_palabras):
    for pivot in range(0,len(lista_palabras)-1):
        for contenido in range(pivot+1,len(lista_palabras)):
            rima(lista_palabras[pivot], lista_palabras[contenido])

lista_palabras = creacion_lista()
verif_rima(lista_palabras)