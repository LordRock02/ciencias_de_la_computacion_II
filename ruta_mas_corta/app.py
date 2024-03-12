from flask import Flask, render_template
from nodo import Nodo
from grafoMunicipios import *

app = Flask(__name__)

@app.route('/')
def hompage():
    return render_template('index.html', municipiosNodo = municipiosNodo)

@app.route('/get-coordenadas', methods=['POST'])
def getCoordenadas():
    coordenadas = {}
    for dep, nodo in municipiosNodo.items():
        nodo:Nodo
        vecinos = {}
        for vecino, dist in nodo.getVecinos().items():
            vecino:Nodo
            vecinos[vecino.getMunicipio().getNombre()] = {
                'latitud':vecino.getMunicipio().getLatitud(),
                'longitud':vecino.getMunicipio().getLongitud()
            }
        coordenadas[dep] = {
            'latitud':nodo.getMunicipio().getLatitud(),
            'longitud':nodo.getMunicipio().getLongitud(),
            'vecinos':vecinos
        }
    return coordenadas

@app.route('/calcular-ruta/<origen>/<destino>/<algoritmo>', methods=['POST'])
def calcularRuta(origen:str, destino:str, algoritmo:str):
    resultado = None
    if algoritmo == 'Dijkstra':
        resultado = getRutaDijkstra(origen, destino)
    elif algoritmo == 'A*':
        resultado = getRutaAStar(origen, destino)
    return resultado

if __name__ == '__main__':
    app.run(debug=True)