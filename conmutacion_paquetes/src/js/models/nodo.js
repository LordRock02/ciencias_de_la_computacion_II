export default class Nodo {
    constructor(_id, _vecinos = {}) {
        this._id = _id
        this._vecinos = _vecinos
    }

    get id() {
        return this._id
    }

    set id(_id) {
        this._id = _id
    }

    get vecinos() {
        return this._vecinos
    }

    set vecinos(_vecinos) {
        this._vecinos = _vecinos
    }

    agregarVecino(idVecino, peso) {
        this._vecinos[idVecino] = peso
    }
}