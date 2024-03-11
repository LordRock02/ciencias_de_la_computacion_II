from nodo import Nodo
from municipio import Municipio
import math

def getDistancia(origen:Municipio, destino:Municipio):
    theta = origen.getLongitud() - destino.getLongitud()
    distancia = 60 * 1.1515 * (180/math.pi) * math.acos(
        math.sin(origen.getLatitud() * (math.pi/180)) * math.sin(destino.getLatitud() * (math.pi/180)) + 
        math.cos(origen.getLatitud() * (math.pi/180)) * math.cos(destino.getLatitud() * (math.pi/180)) *
        math.cos(theta * (math.pi/180))
    )
    return distancia*1.609344

class Grafo:
    
    def __init__(self, nodos={}):
        self.__nodos = nodos

    
    def getNodoPesoMenor(self, pesos, visitados):
        nodoPesoMenor:Nodo = None
        for nodo, peso in pesos.items():
            if peso != 'infinity':
                if nodo not in visitados:
                    if nodoPesoMenor is None:
                        nodoPesoMenor = nodo
                    if peso < pesos[nodoPesoMenor]:
                        nodoPesoMenor = nodo
        return nodoPesoMenor

    def dijkstra(self, nodoInicio:Nodo, nodoDestino:Nodo):
        pesos = {}
        nodoAnt = {
            nodoInicio:None
        }
        visitados = []
        for clave, nodo in self.__nodos.items():
            if nodo != nodoInicio:
                pesos[nodo] = float('inf')
            else:
                pesos[nodo] = 0
        
        nodo:Nodo = nodoInicio

        while(nodo):
            for n, dist in nodo.getVecinos().items():
                n:Nodo
                if n != nodoInicio:
                    if(pesos[n] == float('inf')):
                        pesos[n] = 0
                        pesos[n] = dist + pesos[nodo]
                        nodoAnt[n] = nodo
                    else:
                        peso = pesos[n] + dist
                        if(peso < pesos[n]):
                            pesos[n] = peso
                            nodoAnt[n] = nodo
            visitados.append(nodo)
            nodo = self.getNodoPesoMenor(pesos,visitados)
        for nodo, peso in pesos.items():
            print(f'destino: {nodo.getMunicipio().getNombre()}\tdistancia: {peso}')
        rutaOptima = [nodoDestino]
        nodo = nodoAnt[nodoDestino]
        while(nodo):
            rutaOptima.append(nodo)
            nodo = nodoAnt[nodo]

        rutaOptima.reverse()

        resultado = {
            'distancia' : pesos[nodoDestino],
            'ruta' : rutaOptima
        }
        return resultado
    
    def A_star(self, nodoInicio:Nodo, nodoDestino:Nodo):
        rutaOptima:list = [nodoInicio]
        nodoActual:Nodo = nodoInicio
        vecinoMasCercano:Nodo = None
        distanciaAcumulada:float = 0
        while(nodoActual != nodoDestino):
            distanciaMinima = float('inf')
            vecinos = nodoActual.getVecinos()
            for n, dist in vecinos.items():
                n:Nodo
                if n not in rutaOptima:
                    distancia = distanciaAcumulada + dist + getDistancia(n.getMunicipio(), nodoDestino.getMunicipio())
                    if distancia < distanciaMinima:
                        distanciaMinima = distancia
                        vecinoMasCercano = n
            
            distanciaAcumulada += vecinos[vecinoMasCercano]
            nodoActual = vecinoMasCercano
            rutaOptima.append(nodoActual)
        resultado = {
            'distancia' : distanciaAcumulada,
            'ruta' : rutaOptima
        }

        return resultado
                        
                        
        
        
        