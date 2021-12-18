import requests
import json

def listar_membresias(id_espacio):
    url = "https://webexapis.com/v1/memberships"
    params = {"roomId": id_espacio}
    resp = requests.get(url, headers=encabezado, params=params)
    resp_json = resp.json()
    print("Id espacio:", id_espacio)
    for item in resp_json["items"]:
        print("-", item["personDisplayName"], item["personEmail"])

def enviar_mensaje(id_espacio):
    url = "https://webexapis.com/v1/messages"
    params = {"roomId": id_espacio, "markdown": "*** Enlace para el contenedor Docker ***"}
    resp = requests.post(url, headers=encabezado, json=params)

# Datos para todas las solicitudes
token_acceso = "ZGUyM2U0Y2YtZmJkNi00NDZmLWFjZDAtZGFlMzdhNjUzYTNkYzExM2E0ZWEtY2Ri_P0A1_242b07f9-2b66-4cc2-9f6c-81cb45ce0742"
encabezado = {"Authorization": "Bearer {}".format(token_acceso), "Content-Type": "application/json"}
titulo = "Devnet-GroupDeltaBeta"

# Solicutud para listar los espacios existentes
url = "https://webexapis.com/v1/rooms"
params = {"max": 100}
resp = requests.get(url, headers=encabezado, params=params)
resp_json = resp.json()
num_esps = 0
for item in resp_json["items"]:
    if item["title"] == titulo:
        id_espacio = item["id"]
        num_esps += 1

# Si el número de espacios es 0, crear un espacio nuevo y agregar a los participantes
if num_esps == 0:
    # Solicitud para crear el espacio
    params = {"title": titulo}
    resp = requests.post(url, headers=encabezado, json=params)
    resp_json = resp.json()
    id_espacio = resp_json["id"]
    
    # Solicitud para las membresías
    url = "https://webexapis.com/v1/memberships"
    correos = ("amendozag88@gmail.com", "gpalomeque123@gmail.com", "jvonlandwust@doc.ulasalle.edu.bo", "diego.zumelzu18@gmail.com") #", rcsa@hotmail.com")
    for correo in correos:
        params = {"roomId": id_espacio, "personEmail": correo}
        resp = requests.post(url, headers=encabezado, json=params)
    listar_membresias(id_espacio)
    enviar_mensaje(id_espacio)
else:
    listar_membresias(id_espacio)
    enviar_mensaje(id_espacio)
