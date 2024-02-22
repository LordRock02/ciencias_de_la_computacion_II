from persona import Persona
class Producto:
    __id:int
    __nombre:str
    __precio:float
    __vendedor:Persona

    def __init__(self, id:int, vendedor:Persona, nombre:str='producto', precio:float=0):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__vendedor = vendedor
    
    def setId(self, id:int):
        self.__id = id
    
    def getId(self):
        return self.__id
    
    def setVendedor(self, vendedor:Persona):
        self.__vendedor = vendedor
    
    def getVendedor(self):
        return self.__vendedor
    
    def setNombre(self, nombre:str):
        self.__nombre = nombre
    
    def getNombre(self):
        return self.__nombre
    
    def setPrecio(self, precio:float):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio
    
    def to_string(self):
        return f'id: {self.__id}, nombre: {self.__nombre}, precio: {self.__precio}'