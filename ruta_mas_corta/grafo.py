from nodo import Nodo
from municipio import Municipio
import math

def getDistancia(origen:Municipio, destino:Municipio):
    distancia:float = 0
    try:
        theta = origen.getLongitud() - destino.getLongitud()
        distancia = 60 * 1.1515 * (180/math.pi) * math.acos(
            math.sin(origen.getLatitud() * (math.pi/180)) * math.sin(destino.getLatitud() * (math.pi/180)) + 
            math.cos(origen.getLatitud() * (math.pi/180)) * math.cos(destino.getLatitud() * (math.pi/180)) *
            math.cos(theta * (math.pi/180))
        )
    except ValueError as error:
        print(f'errror origen:{origen.getNombre()}, destino: {destino.getNombre()}')

    return distancia*1.609344

class Grafo:
    
    def __init__(self, nodos={}):
        self.__nodos = nodos

    #funcion para escoger el siguiente nodo con el menor peso posible
    def getNodoPesoMenor(self, pesos, visitados):
        nodoPesoMenor:Nodo = None
        for nodo, peso in pesos.items():
            if peso != float('inf'):
                if nodo not in visitados:#filtra por los nodos que no han sido visitados
                    if nodoPesoMenor is None:
                        nodoPesoMenor = nodo
                    if peso < pesos[nodoPesoMenor]:
                        nodoPesoMenor = nodo
        return nodoPesoMenor

    def dijkstra(self, nodoInicio:Nodo, nodoDestino:Nodo):
        pesos = {}#diccionario de pesos
        nodoAnt = {#diccionario de los nodos anteriores
            nodoInicio:None
        }
        visitados = []#lista de nodos visitados
        for clave, nodo in self.__nodos.items():
            if nodo != nodoInicio:
                pesos[nodo] = float('inf')
            else:
                pesos[nodo] = 0
        
        nodo:Nodo = nodoInicio

        while(nodo):#mientras nodo no sea nulo
            for n, dist in nodo.getVecinos().items():#itera vecinos
                n:Nodo
                if n != nodoInicio:
                    if(pesos[n] == float('inf')):#si nodo n(vecino de nodo) no tiene peso asignado 'infinito' se asigna distancia nodo-n
                        pesos[n] = 0
                        pesos[n] = dist + pesos[nodo]
                        nodoAnt[n] = nodo
                    else:
                        peso = pesos[n] + dist
                        if(peso < pesos[n]):#si peso actual es menor que el peso anterio de n, se establece nuevo peso
                            pesos[n] = peso
                            nodoAnt[n] = nodo#se establece nodo como nuevo antecesor de su nodo vecino
            visitados.append(nodo)
            nodo = self.getNodoPesoMenor(pesos,visitados)#se escoge siguiente nodo
        '''for nodo, peso in pesos.items():
            print(f'destino: {nodo.getMunicipio().getNombre()}\tdistancia: {peso}')'''
        rutaOptima = [nodoDestino]
        nodo = nodoAnt[nodoDestino]
        while(nodo):
            rutaOptima.append(nodo)#se llena ruta optima con todos los antecesores de nodoDEstino
            nodo = nodoAnt[nodo]

        rutaOptima.reverse()#reversa ruta

        resultado = {
            'distancia' : pesos[nodoDestino],
            'ruta' : rutaOptima
        }
        return resultado
    
    def A_star(self, nodoInicio:Nodo, nodoDestino:Nodo):
        rutaOptima:list = [nodoInicio]
        nodosDescartados:list[Nodo] = []#lista de nodos por los cuales no puede estar la ruta 
        nodoActual:Nodo = nodoInicio
        vecinoMasCercano:Nodo = None
        distanciaAcumulada:float = 0
        while(nodoActual != nodoDestino):
            distanciaMinima = float('inf')
            vecinos = nodoActual.getVecinos()
            descartar = True#bandera para descartar un nodo
            for n, dist in vecinos.items():#itera nodos vecinos de nodoActual
                n:Nodo
                if n not in rutaOptima and n not in nodosDescartados:#si el nodo no esta en la ruta y en la lista de descartados
                    descartar = False
                    distancia = distanciaAcumulada + dist + getDistancia(n.getMunicipio(), nodoDestino.getMunicipio())
                    if n.getVecinos() or n is nodoDestino:#si el diccionario de vecinos no es vacio ni es el nodoDestino
                        if distancia < distanciaMinima:#se compara la distancia con la distanciaMinima ya establecida
                            distanciaMinima = distancia
                            vecinoMasCercano = n
                    elif not n.getVecinos():#si el nodo 'n' no tiene vecinos se descarta de la ruta
                        nodosDescartados.append(n)
            if not descartar:#si el nodo no ha sido descartado, el vecinoMasCercano se añade a la rutaOptima
                distanciaAcumulada += vecinos[vecinoMasCercano]
                nodoActual = vecinoMasCercano
                rutaOptima.append(nodoActual)
            else:#se descarta el nodo y se hace backtracking de la rutaOptima
                aux:Nodo = rutaOptima.pop()
                nodosDescartados.append(nodoActual)
                aux1:Nodo = rutaOptima.pop()
                vecinos = aux1.getVecinos()
                distanciaAcumulada -= vecinos[aux]
                rutaOptima.append(aux1)
                nodoActual = aux1
        resultado = {
            'distancia' : distanciaAcumulada,
            'ruta' : rutaOptima
        }

        return resultado
                        
                        
        
        
        