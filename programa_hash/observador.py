from abc import ABC, abstractmethod

class Observador(ABC):
    transaccionesHash:list[list]
    @abstractmethod
    def actualizar(self, hashTransacciones:list[list]):
        pass