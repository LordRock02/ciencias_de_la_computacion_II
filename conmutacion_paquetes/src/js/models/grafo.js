import Nodo from "./nodo.js"
export default class Grafo {
    constructor(_nodos = []) {
        this._nodos = _nodos
    }

    get nodos() {
        return this._nodos
    }

    set nodos(_nodos) {
        this._nodos = _nodos
    }

    obtenerNodo(idNodo) {
        for (let nodo of this._nodos) {
            if (nodo instanceof Nodo) {
                if (nodo.id == idNodo) {
                    return nodo
                }
            }
        }
        return null
    }

    agregarVecinosNodo(idNodo, idVecinos) {
        const nodo = this.obtenerNodo(idNodo)
        if (!nodo) {
            console.log(`el nodo ${idNodo} al que intenta acceder no existe`)
            return null
        }
        for (let idVecino in idVecinos) {
            const vecino = this.obtenerNodo(idVecino)
            if (vecino) {
                nodo.agregarVecino(idVecino, idVecinos[idVecino])
                vecino.agregarVecino(idNodo, idVecinos[idVecino])
            } else {
                console.log(`el nodo ${idVecino} al que intenta acceder no existe`)
            }
        }
    }
}