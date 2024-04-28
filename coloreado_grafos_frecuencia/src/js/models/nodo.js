const tipos = {
    borde: 1,
    nucleo: 2
}
export default class Nodo {
    constructor(_id, _color = null, _tipo = 'nucleo', _vecinos = {}, _paquete = {}) {
        this._id = _id
        this._color = _color
        this._vecinos = _vecinos
        this._tipo = tipos[_tipo]
        this._paquete = _paquete
        this._queue = []
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

    get tipo() {
        return this._tipo
    }

    set tipo(_tipo) {
        this._tipo = tipos[_tipo]
    }

    get paquete() {
        return this._paquete
    }

    set paquete(_paquete) {
        this._paquete = _paquete
    }

    get queue() {
        return this._queue
    }

    set queue(_queue){
        this._queue = _queue
    }

    enqueue(_paquete){
        this._queue.push(_paquete)
    }

    dequeue(){
        this.paquete = this.queue.shift()
        console.log(JSON.stringify(this._queue, null, 2))
        if(this.paquete == undefined){
            this.paquete = {}
        }
    }

    agregarVecino(idVecino, frecuencia) {
        this._vecinos[idVecino] = frecuencia
    }
}