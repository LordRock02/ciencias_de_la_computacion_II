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

    actualizarAristas() {
        //console.log('actualizar aristas')
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

    enviarVecino(idOrigen, idDestino) {
        if (idOrigen != idDestino) {
            let origen = this.obtenerNodo(idOrigen)
            let vecino = null
            let costoMinimo = Infinity
            let costoAcumulado = 0
            costoAcumulado = origen.paquete.costo
            for (let vecinoId in origen.vecinos) {
                let costo = costoAcumulado + (1 / origen.vecinos[vecinoId])
                if (costoMinimo > costo || vecinoId == idDestino) {
                    costoMinimo = costo
                    vecino = vecinoId
                    console.log(`vecino ${vecino}`)
                    if(vecinoId == idDestino){
                        break
                    }
                }
            }
            if (vecino == idDestino) {
                console.log('se termino')
            }
            origen.paquete.recorrido.push(vecino)
            origen.paquete.costo = costoMinimo
            vecino = this.obtenerNodo(vecino)
            vecino.paquete = origen.paquete
            origen.paquete = {}
            return vecino.id
        }
        return null
    }
}