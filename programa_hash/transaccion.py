from persona import Persona
from producto import Producto

class Transaccion:
    __id:int
    __producto:Producto
    __vendedor:Persona
    __comprador:Persona
    __fecha:str

    def __init__(self, producto, vendedor, comprador, id = 0, fecha = 0):
        self.__id = id
        self.__producto = producto
        self.__vendedor = vendedor
        self.__comprador = comprador
        self.__fecha = fecha

    def setId(self, id):
        self.__id = id
    def getId(self):
        return self.__id
    def setProducto(self, producto):
        self.__producto = producto
    def getProducto(self):
        return self.__producto
    def setVendedor(self, vendedor):
        self.__vendedor = vendedor
    def getVendedor(self):
        return self.__vendedor
    def setComprador(self, comprador):
        self.__comprador = comprador
    def getComprador(self):
        return self.__comprador
    def setFecha(self, fecha):
        self.__fecha = fecha
    def getFecha(self):
        return self.__fecha