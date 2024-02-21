from observador import Observador

class PortaTransacciones:
    __observadores:list[Observador]=[]
    
    def __init__(self):
        pass

    def agregarObservador(self, observador:Observador):
        self.__observadores.append(observador)

    def quitarObservador(self, observador:Observador):
        self.__observadores.remove(observador)

    def notificarObservadores(self, hashTransacciones:list[list]):
        for observador in self.__observadores:
            observador.actualizar(hashTransacciones)