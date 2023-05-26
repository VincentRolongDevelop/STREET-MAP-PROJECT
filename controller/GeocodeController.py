import http.server
import requests
import json

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    key = "32efpKKQxCSJchjYCMwAuREIB7ywAOAd"
    def do_GET(self, location):
        if self.path == '/api':
            response = self.get_external_data(self.key, location)
            if response is not None:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b'Error al obtener los datos de la API externa')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Error 404: Not Found')

    def get_external_data(self, key, location):
        try:
            response = requests.get('https://www.mapquestapi.com/geocoding/v1/address?key='+key+'&location='+location)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException:
            return None

def run_server():
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyRequestHandler)
    print('Servidor en ejecución...')
    httpd.serve_forever()

run_server()
