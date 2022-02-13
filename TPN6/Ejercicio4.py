# Ejercicio 4: Escribir una clase en python que obtenga todas las posibles sublistas únicas de una lista de
# números enteros distintos. No tener en cuenta una lista vacía.

# Entrada: [4, 5, 6]
# Salida: [[6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class Lista:
    def __init__(self, lista):
        self.lista = lista

    def __repr__(self):
        return f'<Lista: {self.lista}>'

    def sub_lista(self):
        sublista = []
        for pivot in range(len(self.lista)):
            for contenido in range(len(self.lista)+1):
                if not self.lista[pivot:contenido] == []:
                    sublista.append(self.lista[pivot:contenido])
        return f'<Sublista: {sublista}>'

lista = Lista([4,5,6])
sublista = lista.sub_lista()
print(lista)
print(sublista)