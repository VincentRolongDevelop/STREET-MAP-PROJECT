import requests
import urllib
import os
import json

def map():  
    continuar = True
    while continuar is True:
        api_url = "https://www.mapquestapi.com/directions/v2/route?"
        key ="Jza27DprNplH026ncxVaDdEhjPRMIP0a"

        origin = input("ingresa el origen: ")
        if origin == 'q':
            break
        destination = input("Ingrese el destino: ")
        if destination == 'q':
            break
        url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination})
        json_data = requests.get(url).json()
        status_code = json_data["info"]["statuscode"]
        if status_code == 0:
            duration = json_data["route"]["formattedTime"]
            distance = json_data["route"]["distance"] * 1.61
            print("==============================")
            print(f"Información del viaje desde: {origin.capitalize()} hasta {destination.capitalize()}")
            print(f"Duración del viaje: {duration.capitalize()}")
            print(f"Distancia del viaje en kilometros: "+ str("{:.2f}".format(distance)))