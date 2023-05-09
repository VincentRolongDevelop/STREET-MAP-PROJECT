import requests
import urllib

api_url = "https://www.mapquestapi.com/directions/v2/route?"
key ="Jza27DprNplH026ncxVaDdEhjPRMIP0a"
origin="Barranquilla"
destination="Cartagena"
url = api_url + urllib.parse.urlencode({"key":key,"from":origin,"to":destination})

