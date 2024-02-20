from persona import Persona
from producto import Producto

class Transaccion:
    __id:int
    __producto:Producto
    __vendedor:Persona
    __comprador:Persona
    __fecha:str
    __hash:str

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
    
    def getHash(self):
        hash_resultado = 0
        # Iterar sobre cada carácter del texto
        for caracter in self.__toString():
            # Sumar el valor ASCII de cada carácter al hash
            hash_resultado += ord(caracter)
        
        # Retorna el hash resultante
        return self.__hash
    
    def __toString(self):
        return f'id: {self.__id}, producto: {self.__producto.getNombre()}, vendedor: {self.__vendedor.getNombre()}, comprador: {self.__comprador.getNombre()}, fecha: {self.__fecha}'
        