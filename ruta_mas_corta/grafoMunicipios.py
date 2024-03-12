from nodo import Nodo
from municipio import Municipio
from grafo import Grafo
import math

def getDistancia(origen:Municipio, destino:Municipio):
    theta = origen.getLongitud() - destino.getLongitud()
    distancia = 60*1.1515*(180/math.pi)*math.acos(
        math.sin(origen.getLatitud() * (math.pi/180)) * math.sin(destino.getLatitud() * (math.pi/180)) + 
        math.cos(origen.getLatitud() * (math.pi/180)) * math.cos(destino.getLatitud() * (math.pi/180)) *
        math.cos(theta * (math.pi/180))
    )
    return distancia*1.609344


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


municipiosNodo['Amazonas'].setVecinos({
    municipiosNodo['Caqueta']: getDistancia(municipiosNodo['Amazonas'].getMunicipio(), municipiosNodo['Caqueta'].getMunicipio()),
    municipiosNodo['Vaupes']: getDistancia(municipiosNodo['Amazonas'].getMunicipio(), municipiosNodo['Vaupes'].getMunicipio()),
})

municipiosNodo['Antioquia'].setVecinos({
    municipiosNodo['Bolivar']: getDistancia(municipiosNodo['Antioquia'].getMunicipio(), municipiosNodo['Bolivar'].getMunicipio()),
    municipiosNodo['Boyaca']: getDistancia(municipiosNodo['Antioquia'].getMunicipio(), municipiosNodo['Boyaca'].getMunicipio()),
    municipiosNodo['Choco']: getDistancia(municipiosNodo['Antioquia'].getMunicipio(), municipiosNodo['Choco'].getMunicipio()),
    municipiosNodo['Santander']: getDistancia(municipiosNodo['Antioquia'].getMunicipio(), municipiosNodo['Santander'].getMunicipio())
})

municipiosNodo['Arauca'].setVecinos({
    municipiosNodo['Casanare']: getDistancia(municipiosNodo['Arauca'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio()),
    municipiosNodo['Boyaca']: getDistancia(municipiosNodo['Arauca'].getMunicipio(), municipiosNodo['Boyaca'].getMunicipio()),
    municipiosNodo['Vichada']: getDistancia(municipiosNodo['Arauca'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio())
})

municipiosNodo['Bolivar'].setVecinos({
    municipiosNodo['Antioquia']: getDistancia(municipiosNodo['Bolivar'].getMunicipio(), municipiosNodo['Antioquia'].getMunicipio()),
    municipiosNodo['Magdalena']: getDistancia(municipiosNodo['Bolivar'].getMunicipio(), municipiosNodo['Magdalena'].getMunicipio())
})

municipiosNodo['Boyaca'].setVecinos({
    municipiosNodo['Antioquia']: getDistancia(municipiosNodo['Boyaca'].getMunicipio(), municipiosNodo['Antioquia'].getMunicipio()),
    municipiosNodo['Arauca']: getDistancia(municipiosNodo['Boyaca'].getMunicipio(), municipiosNodo['Arauca'].getMunicipio()),
    municipiosNodo['Casanare']: getDistancia(municipiosNodo['Boyaca'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio()),
    municipiosNodo['Cundinamarca']: getDistancia(municipiosNodo['Boyaca'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio()),
    municipiosNodo['Santander']: getDistancia(municipiosNodo['Boyaca'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio())
})

municipiosNodo['Caqueta'].setVecinos({
    municipiosNodo['Amazonas']: getDistancia(municipiosNodo['Caqueta'].getMunicipio(), municipiosNodo['Amazonas'].getMunicipio()),
    municipiosNodo['Huila']: getDistancia(municipiosNodo['Caqueta'].getMunicipio(), municipiosNodo['Huila'].getMunicipio()),
    municipiosNodo['Meta']: getDistancia(municipiosNodo['Caqueta'].getMunicipio(), municipiosNodo['Meta'].getMunicipio())
})

municipiosNodo['Casanare'].setVecinos({
    municipiosNodo['Arauca']: getDistancia(municipiosNodo['Casanare'].getMunicipio(), municipiosNodo['Arauca'].getMunicipio()),
    municipiosNodo['Boyaca']: getDistancia(municipiosNodo['Casanare'].getMunicipio(), municipiosNodo['Boyaca'].getMunicipio()),
    municipiosNodo['Meta']: getDistancia(municipiosNodo['Casanare'].getMunicipio(), municipiosNodo['Meta'].getMunicipio()),
    municipiosNodo['Vichada']: getDistancia(municipiosNodo['Casanare'].getMunicipio(), municipiosNodo['Vichada'].getMunicipio())
})

municipiosNodo['Cauca'].setVecinos({
    municipiosNodo['Nariño']: getDistancia(municipiosNodo['Cauca'].getMunicipio(), municipiosNodo['Nariño'].getMunicipio()),
    municipiosNodo['Huila']: getDistancia(municipiosNodo['Cauca'].getMunicipio(), municipiosNodo['Huila'].getMunicipio())
})

municipiosNodo['Choco'].setVecinos({
    municipiosNodo['Antioquia']: getDistancia(municipiosNodo['Choco'].getMunicipio(), municipiosNodo['Antioquia'].getMunicipio())
})

municipiosNodo['Cundinamarca'].setVecinos({
    municipiosNodo['Boyaca']: getDistancia(municipiosNodo['Cundinamarca'].getMunicipio(), municipiosNodo['Boyaca'].getMunicipio()),
    municipiosNodo['Meta']: getDistancia(municipiosNodo['Cundinamarca'].getMunicipio(), municipiosNodo['Meta'].getMunicipio()),
    municipiosNodo['Huila']: getDistancia(municipiosNodo['Cundinamarca'].getMunicipio(), municipiosNodo['Huila'].getMunicipio())
})

municipiosNodo['Guainia'].setVecinos({
    municipiosNodo['Vichada']: getDistancia(municipiosNodo['Guainia'].getMunicipio(), municipiosNodo['Vichada'].getMunicipio()),
    municipiosNodo['Vaupes']: getDistancia(municipiosNodo['Guainia'].getMunicipio(), municipiosNodo['Vaupes'].getMunicipio())
})

municipiosNodo['Huila'].setVecinos({
    municipiosNodo['Caqueta']: getDistancia(municipiosNodo['Huila'].getMunicipio(), municipiosNodo['Caqueta'].getMunicipio()),
    municipiosNodo['Cauca']: getDistancia(municipiosNodo['Huila'].getMunicipio(), municipiosNodo['Cauca'].getMunicipio()),
    municipiosNodo['Meta']: getDistancia(municipiosNodo['Huila'].getMunicipio(), municipiosNodo['Meta'].getMunicipio()),
    municipiosNodo['Cundinamarca']: getDistancia(municipiosNodo['Huila'].getMunicipio(), municipiosNodo['Cundinamarca'].getMunicipio())
})

municipiosNodo['La Guajira'].setVecinos({
    municipiosNodo['Magdalena']: getDistancia(municipiosNodo['La Guajira'].getMunicipio(), municipiosNodo['Magdalena'].getMunicipio())
})

municipiosNodo['Magdalena'].setVecinos({
    municipiosNodo['Bolivar']: getDistancia(municipiosNodo['Magdalena'].getMunicipio(), municipiosNodo['Bolivar'].getMunicipio()),
    municipiosNodo['La Guajira']: getDistancia(municipiosNodo['Magdalena'].getMunicipio(), municipiosNodo['La Guajira'].getMunicipio())
})

municipiosNodo['Meta'].setVecinos({
    municipiosNodo['Casanare']: getDistancia(municipiosNodo['Meta'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio()),
    municipiosNodo['Caqueta']: getDistancia(municipiosNodo['Meta'].getMunicipio(), municipiosNodo['Caqueta'].getMunicipio()),
    municipiosNodo['Cundinamarca']: getDistancia(municipiosNodo['Meta'].getMunicipio(), municipiosNodo['Cundinamarca'].getMunicipio()),
    municipiosNodo['Huila']: getDistancia(municipiosNodo['Meta'].getMunicipio(), municipiosNodo['Huila'].getMunicipio())
})

municipiosNodo['Nariño'].setVecinos({
    municipiosNodo['Cauca']: getDistancia(municipiosNodo['Nariño'].getMunicipio(), municipiosNodo['Cauca'].getMunicipio())
})

municipiosNodo['Norte de Santander'].setVecinos({
    municipiosNodo['Santander']: getDistancia(municipiosNodo['Norte de Santander'].getMunicipio(), municipiosNodo['Santander'].getMunicipio())
})

municipiosNodo['Santander'].setVecinos({
    municipiosNodo['Norte de Santander']: getDistancia(municipiosNodo['Santander'].getMunicipio(), municipiosNodo['Norte de Santander'].getMunicipio()),
    municipiosNodo['Boyaca']: getDistancia(municipiosNodo['Santander'].getMunicipio(), municipiosNodo['Boyaca'].getMunicipio()),
    municipiosNodo['Antioquia']: getDistancia(municipiosNodo['Santander'].getMunicipio(), municipiosNodo['Antioquia'].getMunicipio())
})

municipiosNodo['Vaupes'].setVecinos({
    municipiosNodo['Amazonas']: getDistancia(municipiosNodo['Vaupes'].getMunicipio(), municipiosNodo['Amazonas'].getMunicipio()),
    municipiosNodo['Guainia']: getDistancia(municipiosNodo['Vaupes'].getMunicipio(), municipiosNodo['Guainia'].getMunicipio()),
    municipiosNodo['La Guajira']: getDistancia(municipiosNodo['Vaupes'].getMunicipio(), municipiosNodo['La Guajira'].getMunicipio())
})

municipiosNodo['Vichada'].setVecinos({
    municipiosNodo['Arauca']: getDistancia(municipiosNodo['Vichada'].getMunicipio(), municipiosNodo['Arauca'].getMunicipio()),
    municipiosNodo['Casanare']: getDistancia(municipiosNodo['Vichada'].getMunicipio(), municipiosNodo['Casanare'].getMunicipio()),
    municipiosNodo['Guainia']: getDistancia(municipiosNodo['Vichada'].getMunicipio(), municipiosNodo['Guainia'].getMunicipio())
})

grafo = Grafo(municipiosNodo)

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
    print(f'segmentos ruta: {segementosRuta}')
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
    print(f'segmentos ruta: {segementosRuta}')
    resultadoAStar = {
        'distancia' : distanciaAStar,
        'ruta' : rutaAStar,
        'segmentosRuta' : segementosRuta
    }
    return resultadoAStar



