from nodo import Nodo
from municipio import Municipio
from municipio import getDistancia
import copy

class Grafo:
    __nodos:dict[str,Nodo]
    __edges:list[dict[float,list[Nodo]]] = []
    def __init__(self, nodos:dict[str,Nodo]={}):
        self.__nodos = nodos
        self.__edges = []

    def setNodos(self, nodos:dict[str,Nodo]):
        self.__nodos = nodos

    def getNodos(self):
        return self.__nodos
    
    def getListaNodos(self):
        listaNodos:list[Nodo] = []
        for municipio, nodo in self.getNodos().items():
            listaNodos.append(nodo)
        return listaNodos
    
    def getEdges(self):
        return self.__edges
    
    def addEdge(self, nodo1:Nodo, nodo2:Nodo, distancia:float):
        if {distancia:[nodo1,nodo2]} not in self.__edges and {distancia:[nodo2,nodo1]} not in self.__edges:
            self.__edges.append({distancia:[nodo1,nodo2]})
            #print(f'la cantidad de aristas es : {len(self.__edges)}')

    def sortEdges(self):
        self.__edges = sorted(self.__edges, key=lambda x: list(x.keys())[0])
    
    def setVecinosNodo(self, nodoMunicipio:str, *vecinosMunicipio:str):
        nodo:Nodo = self.__nodos[nodoMunicipio]
        vecino:Nodo
        for vecinoMunicipio in vecinosMunicipio:
            vecino = self.__nodos[vecinoMunicipio]
            nodo.addVecino(vecino)
            self.addEdge(nodo, vecino, nodo.getPesoVecino(vecino))
            #self.addEdge(nodo.getMunicipio().getNombre(), vecino.getMunicipio().getNombre(), nodo.getPesoVecino(vecino))
        #print(len(self.__edges))

    #funcion para escoger el siguiente nodo con el menor peso posible
    def getNodoPesoMenor(self, vecinos:dict[Nodo,float], visitados):
        nodoPesoMenor:Nodo = None
        for nodo, peso in vecinos.items():
            if peso != float('inf'):
                if nodo not in visitados:#filtra por los nodos que no han sido visitados
                    if nodoPesoMenor is None:
                        nodoPesoMenor = nodo
                    if peso < vecinos[nodoPesoMenor]:
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
    
    def bellman_Ford(self, nodoInicio:Nodo, nodoDestino:Nodo):
        pesos = {}#diccionario de pesos
        nodoAnt = {#diccionario de los nodos anteriores
            nodoInicio:None
        }
        #visitados = []#lista de nodos visitados
        for clave, nodo in self.__nodos.items():
            if nodo != nodoInicio:
                pesos[nodo] = float('inf')
            else:
                pesos[nodo] = 0
        
        edges:list = self.__edges.copy()
        for edge in edges:
            for dist, nodos in dict(edge).items():
                if nodos:
                    edges.append({dist: nodos.reverse()})
        edges = sorted(edges, key=lambda x: list(x.keys())[0])
        nodo:Nodo = nodoInicio

        for _ in range(len(self.getListaNodos()) -1):
            for edge in edges:
                for dist, nodos in dict(edge).items():
                    if nodos:
                        nodos:list[Nodo]
                        if pesos[nodos[0]] != float('inf') and pesos[nodos[0]] + dist < pesos[nodos[1]]:
                            pesos[nodos[1]] = pesos[nodos[0]] + dist
                            nodoAnt[nodos[1]] = nodos[0]
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
        print(nodoAnt)
        return resultado
    
    def Kruskal(self):
        nodos:dict[str,Nodo] = copy.deepcopy(self.__nodos)
        #print(f'copia: {nodos["Amazonas"].getVecinos()} - Original: {self.__nodos["Amazonas"].getVecinos()}')
        spanningTree:'Grafo'
        #se vacian los pesos del grafo
        for municipio, nodo in nodos.items():
            nodos[municipio].setVecinos({})
        spanningTree = Grafo(nodos)
        self.sortEdges()
        for edge in self.__edges:
            for peso, listaNodos in edge.items():
                if not self.verificarCiclo(listaNodos[0].getMunicipio().getNombre(), listaNodos[1].getMunicipio().getNombre(), spanningTree):
                    spanningTree.setVecinosNodo(listaNodos[0].getMunicipio().getNombre(), listaNodos[1].getMunicipio().getNombre())
                    spanningTree.setVecinosNodo(listaNodos[1].getMunicipio().getNombre(), listaNodos[0].getMunicipio().getNombre())
                    print(spanningTree.getNodos()[listaNodos[0].getMunicipio().getNombre()])
        return spanningTree.getNodos()
    
    def prim(self, nodoInicial:Nodo):
        nodos:dict[str,Nodo] = copy.deepcopy(self.__nodos)#copia grafo original
        spanningTree:'Grafo'
        for municipio, nodo in nodos.items():#se vacian los vecinos del grafo
            nodos[municipio].setVecinos({})
        spanningTree = Grafo(nodos)
        noVisitados:list[Nodo] = self.getListaNodos()
        noVisitados.remove(nodoInicial)
        nodosVisitados:list[Nodo] = []
        nodo1:Nodo = nodoInicial
        nodo2:Nodo = self.getNodoPesoMenor(nodo1.getVecinos(), nodosVisitados)
        while noVisitados:
            if nodo1 not in nodosVisitados:
                nodosVisitados.append(nodo1)
            municipio1 = nodo1.getMunicipio().getNombre()
            municipio2 = nodo2.getMunicipio().getNombre()
            if not self.verificarCiclo(spanningTree.getNodos()[municipio1].getMunicipio().getNombre(), spanningTree.getNodos()[municipio2].getMunicipio().getNombre(), spanningTree):#verifica si hay ciclo
                spanningTree.setVecinosNodo(municipio1, municipio2)
                spanningTree.setVecinosNodo(municipio2, municipio1)
                noVisitados.remove(nodo2)
                if nodo2 not in nodosVisitados:
                    nodosVisitados.append(nodo2)
            nodo1 = None
            for nodo in nodosVisitados:
                if nodo1 is None:
                    if self.getNodoPesoMenor(nodo.getVecinos(), nodosVisitados) is not None:#verifica que los vecinos de nodo sean validos
                        nodo1 = nodo
                        nodo2 = self.getNodoPesoMenor(nodo1.getVecinos(), nodosVisitados)
                else:
                    if self.getNodoPesoMenor(nodo.getVecinos(), nodosVisitados) != None and self.getNodoPesoMenor(nodo1.getVecinos(), nodosVisitados) != None:#verifica cada uno de los vecinos si son validos o no
                        peso1 = nodo.getPesoVecino(self.getNodoPesoMenor(nodo.getVecinos(), nodosVisitados))
                        peso2 = nodo1.getPesoVecino(self.getNodoPesoMenor(nodo1.getVecinos(), nodosVisitados))
                        if peso1 < peso2:
                            nodo1 = nodo
                            nodo2 = self.getNodoPesoMenor(nodo.getVecinos(), nodosVisitados)
        return spanningTree.getNodos()
    
    def verificarCiclo(self, municipio1:str, municipio2:str, grafo:'Grafo'):
        nodo1:Nodo = grafo.getNodos()[municipio1]
        nodo2:Nodo = grafo.getNodos()[municipio2]
        nodosProcesados:list[Nodo] = []
        pilaVecinos:list[Nodo] = [nodo1]
        while pilaVecinos:
            nodo:Nodo = pilaVecinos.pop()
            if nodo != nodo2:
                print(f'nodo: {nodo.getMunicipio().getNombre()}')
                for vecino, peso in nodo.getVecinos().items():
                    if vecino not in nodosProcesados:
                        nodosProcesados.append(nodo)
                        pilaVecinos.append(vecino)
            else:
                print('hay Ciclo')
                return True
            print('no hay ciclo')
        return False
    