# Ejercicio 6: Definir una función que extraiga el título de una página web.
# Investigar sobre las librerías integradas requests y BeautifulSoup. (WebScraping)

import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.google.com')

pagina = BeautifulSoup(response.text, 'lxml')

print(pagina.title)