export default class Nodo {
    constructor(_id, _color = null, _vecinos = {},) {
        this._id = _id
        this._color = _color
        this._vecinos = _vecinos
    }

    get id() {
        return this._id
    }

    set id(_id) {
        this._id = _id
    }

    get color() {
        return this._color
    }

    set color(_color) {
        this._color = _color
    }

    get vecinos() {
        return this._vecinos
    }

    set vecinos(_vecinos) {
        this._vecinos = _vecinos
    }

    get grado(){
        return Object.keys(this._vecinos).length
    }

    agregarVecino(idVecino, frecuencia) {
        this._vecinos[idVecino] = frecuencia
    }
}