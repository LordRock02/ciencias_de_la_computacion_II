import Nodo from "./nodo.js"
export default class Grafo {
    constructor(_nodos = []) {
        if (_nodos instanceof Array) {
            this._nodos = _nodos
        }
    }

    get nodos() {
        return this._nodos
    }

    set nodos(_nodos) {
        this._nodos = _nodos
    }

    get orden() {
        return this._nodos.length
    }

    crearNodo() {
        const nodo = new Nodo(this._nodos[this._nodos.length - 1].id + 1)
        this._nodos.forEach(vecino => {
            const frecuencia = Math.floor(Math.random() * (300 - 50)) + 50
            nodo.agregarVecino(vecino.id, frecuencia)
            this.obtenerNodo(vecino.id).agregarVecino(nodo.id, frecuencia)
        })
        this._nodos.push(nodo)
    }

    eliminarNodo(id) {
        this._nodos.forEach(nodo => delete nodo.vecinos[id])
        const nodo = this.obtenerNodo(id)
        if (nodo != null) {
            this._nodos.splice(this._nodos.indexOf(nodo))
        }
    }

    listaIdNodos() {
        let nodos = []
        this._nodos.forEach(nodo => nodos.push(nodo.id))
        return nodos
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

    actualizarAristas() {
        let aristasVisitadas = []
        for (let nodo of this._nodos) {
            if (nodo instanceof Nodo) {
                let vecinos = nodo.vecinos
                nodo.vecinos = {}
                for (let idVecino in vecinos) {
                    if (!aristasVisitadas.some(([id1, id2]) => id1 === idVecino && id2 === nodo.id)) {
                        let vecino = this.obtenerNodo(idVecino)
                        if (nodo.tipo == 1 || vecino.tipo == 1) {
                            vecinos[idVecino] = Math.floor(Math.random() * (30 - 10)) + 10
                        }
                        else {
                            vecinos[idVecino] = Math.floor(Math.random() * (120 - 80)) + 80
                        }
                        aristasVisitadas.push([nodo.id, idVecino])
                    } else {
                        delete vecinos[idVecino]
                    }
                }
                this.agregarVecinosNodo(nodo.id, vecinos)
            }
        }
    }
    // devulevue numero de coloreado del grafo
    coloreadoGrafo() {
        this._nodos.forEach(nodo => nodo.color = null)
        let numColores = 1
        for (let nodo of this._nodos) {
            let color = 0
            if (nodo instanceof Nodo) {
                for (let vecinoId in nodo.vecinos) {
                    if (nodo.vecinos[vecinoId] < 150) {
                        let vecino = this.obtenerNodo(vecinoId)
                        if (vecino.color == color) {
                            color++
                        }
                        if (color + 1 > numColores) {
                            numColores = color + 1
                        }
                    }
                }
                nodo.color = color
            }
        }
        return numColores
    }
}