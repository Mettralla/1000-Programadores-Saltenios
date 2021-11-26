# Ejercicio 7: Crear una función que convierta una cadena de texto JSON en un
# diccionario. Usaremos la página http://ip-api.com que devuelve datos de una IP
# pública en formato json. La ip que consultaremos será una de la UNSa.
# IP 170.210.200.2 y url http://ip-api.com/json/170.210.200.2

import json

datos = """
{
    "query": "170.210.200.2",
    "status": "success",
    "continent": "South America",
    "continentCode": "SA",
    "country": "Argentina",
    "countryCode": "AR",
    "region": "A",
    "regionName": "Salta",
    "city": "Salta",
    "district": "",
    "zip": "4400",
    "lat": -24.7792,
    "lon": -65.422,
    "timezone": "America/Argentina/Salta",
    "offset": -10800,
    "currency": "ARS",
    "isp": "Red de Interconexion Universitaria",
    "org": "Red de Interconexion Universitaria",
    "as": "AS4270 Red de Interconexion Universitaria",
    "asname": "Red de Interconexion Universitaria",
    "mobile": false,
    "proxy": false,
    "hosting": false
}
"""

json.loads(datos)