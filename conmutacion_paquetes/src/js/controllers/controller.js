import Grafo from "../models/grafo.js";
import View from "../views/view.js";
import { dibujaGrafo } from "./dibujaGrafo.js";

const limitePaquete = 1
const delayEntrada = 1500
const delayEnvio = 2000
let contador = 0

const sleep = (ms) => {
    return new Promise(resolve => setTimeout(resolve, ms))
}

const dividirPaquete = (mensaje) => {
    let paquetes = []
    if (mensaje instanceof Array) {
        for (let i = 0, index = 0; i < mensaje.length; i += limitePaquete, index++) {
            paquetes.push({ 'index': index, 'contenido': mensaje.slice(i, i + limitePaquete), 'recorrido': [], 'costo': 0 })
        }
        console.log(`funcion dividirPaquete: ${JSON.stringify(paquetes, null, 2)}`)
        return paquetes
    }
    return null
}

const createRow = (counter, message, idNodo, recorrido) => {
    let newRow = document.createElement('tr')
    newRow.innerHTML = `
    <th scope='row'>${counter}</th>
    <td>${message}</td>
    <td>${idNodo}</td>
    <td>${recorrido}</td>`
    return (newRow)
}

export default class Controller {
    constructor(grafo, view) {
        if (grafo instanceof Grafo) {
            this.grafo = grafo
        }
        if (view instanceof View) {
            this.view = view
        }
        this.view.bindSendMessage(this.enviarMensaje.bind(this))
        this.renderGrafo()
    }
    handleTable() {
        this.renderTable()
    }
    async renderTable(message, idNodo, recorrido) {
        //console.log(`mensaje : ${message}`)
        this.view.updateTable(createRow(++contador, message, idNodo, recorrido))
    }
    async renderGrafo() {
        while (true) {
            this.view.canvasGrafo.getContext('2d').clearRect(0, 0, this.view.canvasGrafo.width, this.view.canvasGrafo.height)
            this.grafo.actualizarAristas()
            dibujaGrafo(this.view.canvasGrafo, this.grafo)
            //console.log(this.grafo)
            await sleep(2000)
        }
    }
    async enviarMensaje() {
        let idOrigen = 1
        let idDestino = 9
        let paquetes = dividirPaquete(this.view.inputMessage.value.split(''))
        for (let paquete of paquetes) {
            let nodo = this.grafo.obtenerNodo(idOrigen)
            paquete.recorrido.push(idOrigen)
            nodo.paquete = paquete
            this.renderTable(paquete.contenido, idOrigen, paquete.recorrido)
            this.enviarPaquete(idOrigen, idDestino)
            await sleep(delayEntrada)
        }
    }
    async enviarPaquete(idOrigen, idDestino) {
        let idNodoActual = this.grafo.enviarVecino(idOrigen, idDestino)
        console.log(idNodoActual)
        if (idNodoActual != idDestino && idNodoActual) {
            await sleep(delayEnvio)
            let nodo = this.grafo.obtenerNodo(idNodoActual)
            console.log(`idNodoActual : ${JSON.stringify(nodo, null, 2)}`)
            this.renderTable(nodo.paquete.contenido, idNodoActual, nodo.paquete.recorrido)
            return this.enviarPaquete(idNodoActual, idDestino)
        } else {
            let nodo = this.grafo.obtenerNodo(idNodoActual)
            this.renderTable(nodo.paquete.contenido, idNodoActual, nodo.paquete.recorrido)
        }
    }
}