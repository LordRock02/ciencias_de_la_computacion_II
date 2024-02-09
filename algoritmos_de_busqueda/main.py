import random, time
import algoritmos_de_busqueda as busqueda
from producto import Producto

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

lista_productos = []

for i in range(8*10**5):
    producto = Producto(i, nombre=productos[random.randint(0,19)], precio=random.randint(50, 1000))
    lista_productos.append(producto)

n=random.randint(0, 799999)
print(f'se buscara el elemento con id: {n}') 
print()

print('=================')
print('busqueda binaria:')
print('=================')
print()

start = time.perf_counter()
print(busqueda.busqueda_binaria(lista_productos,n).to_string())
finish = time.perf_counter()
tiempo_binario = finish - start
print(f'tiempo total: {tiempo_binario}')

start = time.perf_counter()
print()
print('====================')
print('busqueda secuencial:')
print('====================')
print()
print(busqueda.busqueda_secuencial(lista_productos,n).to_string())
finish = time.perf_counter()
tiempo_secuencial = finish - start
print(f'tiempo total: {tiempo_secuencial}')
print()
print('==================')
print('R E S U L T A D O:')
print('==================')
print()
print()
print('======================================================================================================')
print(f'la busqueda binaria le tomo {tiempo_binario/tiempo_secuencial} veces el tiempo de busqueda secuencial')
print('======================================================================================================')
print()



