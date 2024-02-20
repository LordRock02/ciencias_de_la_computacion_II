from persona import Persona
class Producto:
    __id:int
    __nombre:str
    __precio:int
    __propietario:Persona

    def __init__(self, id:int, propietario:Persona, nombre:str='producto', precio:int=0):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__propietario = propietario
    
    def setId(self, id:int):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def setPropietario(self, propietario:Persona):
        self.__propietario = propietario
    
    def getPropietario(self):
        return self.__propietario
    
    def setNombre(self, nombre:str):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setPrecio(self, precio:int):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio
    
    def to_string(self):
        return f'id: {self.__id}, nombre: {self.__nombre}, precio: {self.__precio}'