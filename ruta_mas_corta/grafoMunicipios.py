from nodo import Nodo
from municipio import Municipio
from grafo import *

municipiosNodo = {
    'Amazonas': Nodo(Municipio(1,'Amazonas', -4.2031647, -69.9630985)),
    'Antioquia': Nodo(Municipio(2, 'Antioquia', 6.244197, -75.6637852)),
    'Arauca': Nodo(Municipio(3, 'Arauca', 7.076882, -70.707921)),
    'Bolivar': Nodo(Municipio(4, 'Bolivar', 10.402379, -75.507077)),
    'Boyaca': Nodo(Municipio(5, 'Boyaca', 5.454516, -73.362031)),
    'Caqueta': Nodo(Municipio(6, 'Caqueta', 0.869005, -72.898842)),
    'Casanare': Nodo(Municipio(7, 'Casanare', 5.758333, -71.572833)),
    'Cauca': Nodo(Municipio(8, 'Cauca', 2.441791, -76.616713)),
    'Choco': Nodo(Municipio(9, 'Choco', 5.252803, -76.834437)),
    'Cundinamarca': Nodo(Municipio(10, 'Cundinamarca', 4.482241, -74.336106)),
    'Guainia': Nodo(Municipio(11, 'Guainia', 2.669581, -68.095396)),
    'Huila': Nodo(Municipio(12, 'Huila', 2.922149, -75.244141)),
    'La Guajira': Nodo(Municipio(13, 'La Guajira', 11.354754, -72.520635)),
    'Magdalena': Nodo(Municipio(14, 'Magdalena', 10.759581, -74.776339)),
    'Meta': Nodo(Municipio(15, 'Meta', 3.272733, -73.087749)),
    'Nariño': Nodo(Municipio(16, 'Nariño', 1.164871, -77.382830)),
    'Norte de Santander': Nodo(Municipio(17, 'Norte de Santander', 7.946527, -72.899791)),
    'Santander': Nodo(Municipio(18, 'Santander', 7.116667, -73.0)),
    'Vaupes': Nodo(Municipio(19, 'Vaupes', 0.855051, -70.812042)),
    'Vichada': Nodo(Municipio(20, 'Vichada', 5.303792, -68.110226))
}

grafo = Grafo(municipiosNodo)

grafo.setVecinosNodo('Amazonas', 'Caqueta', 'Vaupes')
grafo.setVecinosNodo('Antioquia', 'Bolivar', 'Boyaca', 'Choco', 'Santander')
grafo.setVecinosNodo('Arauca', 'Casanare', 'Boyaca', 'Vichada')
grafo.setVecinosNodo('Bolivar', 'Antioquia', 'Magdalena')
grafo.setVecinosNodo('Boyaca', 'Antioquia', 'Arauca', 'Casanare', 'Cundinamarca', 'Santander')
grafo.setVecinosNodo('Caqueta', 'Amazonas', 'Huila', 'Meta')
grafo.setVecinosNodo('Casanare', 'Arauca', 'Boyaca', 'Meta', 'Vichada')
grafo.setVecinosNodo('Cauca', 'Nariño', 'Huila')
grafo.setVecinosNodo('Choco', 'Antioquia')
grafo.setVecinosNodo('Cundinamarca', 'Boyaca', 'Meta', 'Huila')
grafo.setVecinosNodo('Guainia', 'Vichada', 'Vaupes')
grafo.setVecinosNodo('Huila', 'Caqueta', 'Cauca', 'Meta', 'Cundinamarca')
grafo.setVecinosNodo('La Guajira', 'Magdalena')
grafo.setVecinosNodo('Magdalena', 'Bolivar', 'La Guajira')
grafo.setVecinosNodo('Meta', 'Casanare', 'Caqueta', 'Cundinamarca', 'Huila')
grafo.setVecinosNodo('Nariño', 'Cauca')
grafo.setVecinosNodo('Norte de Santander', 'Santander')
grafo.setVecinosNodo('Santander', 'Norte de Santander', 'Boyaca', 'Antioquia')
grafo.setVecinosNodo('Vaupes', 'Amazonas', 'Guainia')
grafo.setVecinosNodo('Vichada', 'Arauca', 'Casanare', 'Guainia')
'''print('=====')
print('EDGES:')
print('=====')
grafo.sortEdges()
print(len(grafo.getEdges()))
for edge in grafo.getEdges():
    print(edge)'''

def getRutaDijkstra(origen: str, destino: str):
    distanciaDijkstra = grafo.dijkstra(municipiosNodo[origen], municipiosNodo[destino])['distancia']
    rutaDijkstra = []
    segementosRuta = []
    nodosRuta:list[Nodo]= grafo.dijkstra(municipiosNodo[origen], municipiosNodo[destino])['ruta']
    for nodo in nodosRuta:
        nodo: Nodo
        rutaDijkstra.append(nodo.getMunicipio().getNombre())
    for i in range(len(nodosRuta)-1):
        segmento = {
            'a':[nodosRuta[i].getMunicipio().getLatitud(), nodosRuta[i].getMunicipio().getLongitud()],
            'b':[nodosRuta[i + 1].getMunicipio().getLatitud(), nodosRuta[i + 1].getMunicipio().getLongitud()]
        }
        segementosRuta.append(segmento)
    resultadoDijkstra = {
        'distancia': distanciaDijkstra,
        'ruta': rutaDijkstra,
        'segmentosRuta': segementosRuta
    }
    return resultadoDijkstra
def getRutaAStar(origen:str, destino:str):
    distanciaAStar = grafo.A_star(municipiosNodo[origen], municipiosNodo[destino])['distancia']
    rutaAStar = []
    segementosRuta = []
    nodosRuta:list[Nodo] = grafo.A_star(municipiosNodo[origen], municipiosNodo[destino])['ruta']
    for nodo in nodosRuta:
        nodo:Nodo
        rutaAStar.append(nodo.getMunicipio().getNombre())
    for i in range(len(nodosRuta)-1):
        segmento = {
            'a':[nodosRuta[i].getMunicipio().getLatitud(), nodosRuta[i].getMunicipio().getLongitud()],
            'b':[nodosRuta[i + 1].getMunicipio().getLatitud(), nodosRuta[i + 1].getMunicipio().getLongitud()]
        }
        segementosRuta.append(segmento)
    resultadoAStar = {
        'distancia' : distanciaAStar,
        'ruta' : rutaAStar,
        'segmentosRuta' : segementosRuta
    }
    return resultadoAStar


def cargarCordenadas(nodos:dict[str,Nodo]):
    coordenadas = {}
    for dep, nodo in nodos.items():
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