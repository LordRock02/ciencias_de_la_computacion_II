from persona import Persona
from observador import Observador

class Testigo(Persona, Observador):

    def __init__(self, id: int, nombre: str):
        super().__init__(id, nombre)

    def actualizar(self):
        '''actualizar tabla hash'''
        return super().actualizar()