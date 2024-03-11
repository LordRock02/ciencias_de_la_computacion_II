from flask import Flask, render_template
from nodo import Nodo
from grafoMunicipios import *

app = Flask(__name__)

@app.route('/')
def hompage():
    return render_template('index.html', municipiosNodo = municipiosNodo)

@app.route('/calcular-ruta/<origen>/<destino>', methods=['POST'])
def calcularRuta(origen, destino):
    resultadoDijkstra = getRutaDijkstra(origen, destino)
    resultadoAStar = getRutaAStar(origen, destino)
    resultado = {
        'dijkstra' : resultadoDijkstra,
        'A*' : resultadoAStar
    }
    '''print(f'dijkstra: {resultadoDijkstra}')
    print(f'algoritmo A*: {resultadoAStar}')'''
    return resultado

if __name__ == '__main__':
    app.run(debug=True)