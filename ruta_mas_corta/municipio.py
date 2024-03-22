import math
class Municipio:
    def __init__(self, id=0, nombre='', latitud=0, longitud=0):
        self.__nombre = nombre
        self.__latitud = latitud
        self.__longitud = longitud
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getLatitud(self):
        return self.__latitud

    def setLatitud(self, latitud):
        self.__latitud = latitud

    def getLongitud(self):
        return self.__longitud

    def setLongitud(self, longitud):
        self.__longitud = longitud

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

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