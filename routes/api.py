from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/api/vehicles')
def get_vehicles():
    return 'getting vehivulos'

@app.get('/api/vehicles/1')
def list_vehicles():
    return 'listed vehivulos'

@app.post('/api/vehicles')
def create_vehicles():
    return 'creating vehiculo'

@app.put('/api/vehicles/1')
def update_vehicles():
    return 'updated vehiculo'

@app.delete('/api/vehicles/1')
def delete_vehicles():
    return 'deleted vehiculo'