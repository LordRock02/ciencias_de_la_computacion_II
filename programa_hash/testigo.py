from persona import Persona
from observador import Observador

class Testigo(Persona, Observador):

    def __init__(self, id: int, nombre: str):
        Persona.__init__(self ,id, nombre)
        Observador.__init__(self)

    def actualizar(self, hashTransacciones):
        self.setTrasaccionesHash(hashTransacciones)
        '''for row in self.getTrasaccionesHash():
            print(row)
        actualizar tabla hash'''