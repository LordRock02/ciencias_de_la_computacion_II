from persona import Persona
from producto import Producto
from observador import Observador

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
        self.__hash = ''
        # Iterar sobre cada carácter del texto
        #print(f'transaccion {self.toString()}')
        for caracter in self.toString():
            # Sumar el valor ASCII de cada carácter al hash
            if ord(caracter) != 40 and ord(caracter) != 41:
                self.__hash += str(ord(caracter))
        
        # Retorna el hash resultante
        return int(self.__hash)
    
    def toString(self):
        return f'{self.__id} {self.__vendedor.getNombre()} {self.__comprador.getNombre()} {self.__producto.getNombre()} {self.__producto.getPrecio()} {self.__fecha}'        