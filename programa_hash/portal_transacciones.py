from observador import Observador
from producto import Producto
from persona import Persona
from transaccion import Transaccion
from testigo import Testigo
from datetime import datetime

class PortaTransacciones:
    __observadores:list[Observador]=[]
    __hashTransacciones:list[list[int]] = [[] for _ in range(10)]
    __totalTransaccioens:int
    
    def __init__(self):
        self.__totalTransaccioens = 0

    def agregarObservador(self, observador:Observador):
        self.__observadores.append(observador)

    def quitarObservador(self, observador:Observador):
        self.__observadores.remove(observador)

    def notificarObservadores(self):
        for observador in self.__observadores:
            if isinstance(observador, Testigo):
                observador.actualizar(self.__hashTransacciones)

    def getHashTransacciones(self):
        return self.__hashTransacciones
    
    def realizarTransaccion(self, comprador:Persona, producto:Producto):
        transaccion = Transaccion(producto, producto.getVendedor(), comprador, id=self.__totalTransaccioens, fecha=datetime.now())
        index = transaccion.getHash()%10
        if(self.__hashTransacciones[index].count(transaccion.getHash()) == 0):
            self.__hashTransacciones[index].append(transaccion.getHash())
            self.__totalTransaccioens += 1
        else:
            print('error la transaccion ya habia sido insertada')
        self.notificarObservadores()
        
    