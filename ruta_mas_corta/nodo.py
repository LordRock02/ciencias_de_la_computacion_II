from municipio import Municipio
from municipio import getDistancia
class Nodo:

    __municipio:Municipio
    __vecinos:dict['Nodo':float]

    def __init__(self, municipio, vecinos={}):
        self.__municipio = municipio
        self.__vecinos = vecinos

    def getMunicipio(self):
        return self.__municipio

    def setMunicipio(self, municipio):
        self.__municipio = municipio

    def getVecinos(self):
        return self.__vecinos

    def setVecinos(self, vecinos):
        self.__vecinos = vecinos

    def addVecino(self, vecino:'Nodo'):
        vecinos:dict['Nodo',float] = self.__vecinos.copy()
        vecinos[vecino] = getDistancia(self.__municipio, vecino.getMunicipio())
        self.__vecinos = vecinos

    def getPesoVecino(self, vecino):
        return self.__vecinos[vecino]