import random
import time
import msvcrt
import algoritmos_de_busqueda as busqueda
from producto import Producto
from transaccion import Transaccion
from persona import Persona
from testigo import Testigo
from portal_transacciones import PortaTransacciones
from datetime import datetime
from observador import Observador


portal = PortaTransacciones()

personas = [
    {"nombre": "Juan"},
    {"nombre": "María"},
    {"nombre": "Carlos"},
    {"nombre": "Ana"},
    {"nombre": "Pedro"},
    {"nombre": "Laura"},
    {"nombre": "Luis"},
    {"nombre": "Sofía"},
    {"nombre": "Miguel"},
    {"nombre": "Elena"}
]

__productos = [
    {"producto": "Camisa", "precio": 25.99},
    {"producto": "Pantalón", "precio": 39.99},
    {"producto": "Zapatos", "precio": 59.99},
    {"producto": "Bolso", "precio": 29.99},
    {"producto": "Reloj", "precio": 99.99},
    {"producto": "Gafas de sol", "precio": 19.99},
    {"producto": "Bufanda", "precio": 14.99},
    {"producto": "Guantes", "precio": 9.99},
    {"producto": "Sombrero", "precio": 24.99},
    {"producto": "Calcetines", "precio": 6.99}
]

vendedores:list[Persona]=[]
productos:list[Producto]=[]
testigos:list[Observador]=[]

for i in range(len(personas)):
    persona = Persona(i, personas[i]['nombre'])
    producto = Producto(i, persona, __productos[i]['producto'], __productos[i]['precio'])
    productos.append(producto)
    vendedores.append(persona)

for i in range(10):
    testigo = Testigo(i, 'testigo'+str(i))
    testigos.append(testigo)
    portal.agregarObservador(testigo)


persona1 = Persona(10, 'roger')
for i in range(5):
    portal.realizarTransaccion(persona1, productos[i])

'''for testigo in testigos:
    print('hola')
    for row in testigo.getTrasaccionesHash():
        print(row)'''
while(True):
    opcion:int
    while(True):
        print('desea realizar una transaccion?')
        print('1.Si\t2.No')
        opcion = int(input())
        if opcion == 1 or opcion==2:
            break
    if opcion == 2:
        break
    print('escoja un Producto:')
    while(True):
        i = 0
        for producto in __productos:
            print(f'[{i}]\tproducto: {producto["producto"]}\tvalor: {producto["precio"]}')
            i += 1
        opcion = int(input())
        if opcion >= 0 and opcion <=9:
            break
    portal.realizarTransaccion(persona1, productos[opcion])
    print('==============')
    print('transacciones:')
    print('==============')
    for transaccion in portal.getHashTransacciones():
        print(transaccion)
    msvcrt.getch()




#print(transaccion.getHash(), datetime.now())



