# Ejercicio 5: A partir del contenido de una página generar un archivo que guarde
# la información extraída. La página contiene una lista de los 40 temas
# principales de música.

import requests
from bs4 import BeautifulSoup

def leer_y_obtener_canciones(url):
    sitio = requests.get(url=url)
    soup = BeautifulSoup(sitio.content)
    return soup

soup = leer_y_obtener_canciones('https://los40.com/los40/2021/02/18/musica/1613476104_405901.html')

canciones = soup.find('div', {'id': 'cuerpo_noticia'}).find_all('h2')

with open('TPN8/archivos/canciones.txt', 'w') as archivo:
    texto = ''
    for cancion in canciones:
        texto += cancion.get_text() + '\n'
    archivo.write(texto)