import random
import algoritmos_de_busqueda as busqueda
from producto import Producto
from transaccion import Transaccion
from persona import Persona
from datetime import datetime

productos = {
    0: "Manzanas",
    1: "Leche",
    2: "Pan",
    3: "Huevos",
    4: "Arroz",
    5: "Aceite de oliva",
    6: "Pollo",
    7: "Pasta",
    8: "Café",
    9: "Jabón",
    10: "Papel higiénico",
    11: "Queso",
    12: "Yogur",
    13: "Cerveza",
    14: "Zanahorias",
    15: "Pescado",
    16: "Papel de cocina",
    17: "Tomates",
    18: "Papel aluminio",
    19: "Cepillo de dientes"
}


persona1 = Persona(1, 'roger')
persona2 = Persona(2, 'luis')

producto = Producto(1, persona1, nombre = productos[10], precio=500)
transaccion = Transaccion(producto,persona1,persona2,id=0, fecha=datetime.now())
print(transaccion.getHash())


