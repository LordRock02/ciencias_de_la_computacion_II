from municipio import Municipio
class Nodo:

    __municipio:Municipio
    __vecinos = {}

    def __init__(self, municipio, vecinos={}):
        self.__municipio = municipio
        self.vecinos = vecinos

    def getMunicipio(self):
        return self.__municipio

    def setMunicipio(self, municipio):
        self.__municipio = municipio

    def getVecinos(self):
        return self.__vecinos

    def setVecinos(self, vecinos):
        self.__vecinos = vecinos

    def getPesoVecino(self, vecino):
        return self.__vecinos[vecino]