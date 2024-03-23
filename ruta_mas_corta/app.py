from flask import Flask, render_template
from nodo import Nodo
from grafoMunicipios import *

app = Flask(__name__)

@app.route('/')
def hompage():
    return render_template('index.html', municipiosNodo = municipiosNodo)

@app.route('/get-coordenadas', methods=['POST'])
def getCoordenadasEndPoint():
    return cargarCordenadas(municipiosNodo)

@app.route('/calcular-ruta/<origen>/<destino>/<algoritmo>', methods=['POST'])
def calcularRutaEndPoint(origen:str, destino:str, algoritmo:str):
    resultado = None
    if algoritmo == 'Dijkstra':
        resultado = getRutaDijkstra(origen, destino)
    elif algoritmo == 'A*':
        resultado = getRutaAStar(origen, destino)
    elif algoritmo == 'Bellman-Ford':
        pass
    return resultado

@app.route('/spanning-tree/<algoritmo>/<nodoInicial>', methods=['POST'])
def spanningTreeEndPoint(algoritmo:str, nodoInicial:Nodo = None):
    print('juanse es gay')
    spanningTree:dict = {}
    if algoritmo == 'Kruskal':
        spanningTree = grafo.Kruskal()
    if algoritmo == 'Prim':
        spanningTree = grafo.prim(grafo.getNodos()[nodoInicial])
    return cargarCordenadas(spanningTree)

if __name__ == '__main__':
    app.run(debug=True)