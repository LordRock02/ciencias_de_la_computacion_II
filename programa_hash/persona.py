class Persona:
    __id:int
    __nombre:str
    def ___init__(self, id:int, nombre:str):
        self.__id = id
        self.__nombre = nombre
    

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre
    
    def setId(self, id:int):
        self.__id = id

    def getId(self):
        return self.__id