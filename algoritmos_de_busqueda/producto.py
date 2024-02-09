class Producto:
    __id:int
    __nombre:str
    __precio:int

    def __init__(self, id:int, nombre:str='producto', precio:int=0):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
    
    def setId(self, id:int):
        self.__id = id
    
    def getId(self):
        return self.__id
    
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