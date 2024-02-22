from abc import ABC, abstractmethod

class Observador(ABC):
    __transaccionesHash:list[list]
    def __init__(self):
        self.__transaccionesHash = [[]]

    @abstractmethod
    def actualizar(self, hashTransacciones):
        pass
    
    def getTrasaccionesHash(self):
        return self.__transaccionesHash
    
    def setTrasaccionesHash(self, transaccionesHash):
        self.__transaccionesHash=transaccionesHash
    