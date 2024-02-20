from producto import Producto
def busqueda_binaria(lista:list, id:int):
    start = 0
    finish = len(lista)
    n = (start + finish)//2
    i = 0
    while True:
        i+=1
        if lista[n].getId() == id:
            print(f'iteraciones busqueda binaria: {i}')
            return lista[n]
        elif lista[n].getId() > id:
            finish = n-1
        else:
            start = n+1
        n = (start + finish)//2


def busqueda_secuencial(lista:list, id:int):
    i = 0
    for p in lista:
        i += 1
        if(p.getId()==id):
            print(f'iteraciones busqueda secuencial: {i}')
            return p