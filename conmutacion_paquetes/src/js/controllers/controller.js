import Grafo from "../models/grafo.js";
import Nodo from "../models/nodo.js";
import View from "../views/view.js";
import { dibujaGrafo } from "./dibujaGrafo.js";
//import {enviarPaquete} from '../utils/enviarPaqueteWorker.js'

const limitePaquete = 3
const delayProceso = 1
const delayEnvio = 2
const ciclo = 2
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
        this.view.bindClearTable(this.clearTable.bind(this))
        this.renderGrafo()
        this.setOpciones()
    }
    setOpciones(){
        let opciones = []
        for(let nodo of this.grafo.nodos){
            if(nodo instanceof Nodo){
                if(nodo.tipo == 1){
                    opciones.push(nodo.id)
                }
            }
        }
        opciones.forEach(idNodo => {
            let opcion = document.createElement('option')
            opcion.text = `Nodo ${idNodo}`
            opcion.value = idNodo
            this.view.selectDestino.appendChild(opcion)

        })
        opciones.forEach(idNodo => {
            let opcion = document.createElement('option')
            opcion.text = `Nodo ${idNodo}`
            opcion.value = idNodo
            this.view.selectOrigen.appendChild(opcion)

        })
    }
    clearTable() {
        this.view.table.innerHTML = ''
    }
    async renderTable(message, idNodo, recorrido) {
        this.view.updateTable(createRow(++contador, message, idNodo, recorrido))
    }
    async renderGrafo() {
        while (true) {
            this.view.canvasGrafo.getContext('2d').clearRect(0, 0, this.view.canvasGrafo.width, this.view.canvasGrafo.height)
            this.grafo.actualizarAristas()
            dibujaGrafo(this.view.canvasGrafo, this.grafo)
            await sleep(ciclo*1000)
        }
    }
    async enviarMensaje() {
        let idOrigen = this.view.selectOrigen.value
        let idDestino = this.view.selectDestino.value
        let nodo = this.grafo.obtenerNodo(idOrigen)
        nodo.queue = dividirPaquete(this.view.inputMessage.value.split(''))
        nodo.queue.forEach(element => element.recorrido.push(idOrigen))
        this.enviarPaquete(idOrigen, idDestino)
    }
    async enviarPaquete(idOrigen, idDestino) {
        let nodoActual = this.grafo.obtenerNodo(idOrigen)
        if (idOrigen != idDestino && idOrigen) {
            while (true) {
                if (nodoActual.queue.length > 0) {
                    await sleep((Math.floor(Math.random() * (delayEnvio - 5)) + 5)*1000)
                    nodoActual.dequeue()
                    console.log(nodoActual)
                    if (nodoActual.paquete != {}) {
                        this.renderTable(nodoActual.paquete.contenido, nodoActual.id, nodoActual.paquete.recorrido)
                        await sleep((Math.floor(Math.random() * (delayProceso - 3)) + 3)*1000)
                        this.enviarPaquete(this.grafo.enviarVecino(idOrigen, idDestino), idDestino)
                    }
                } else {
                    break
                }
            }
        } else {
            nodoActual.dequeue()
            this.renderTable(nodoActual.paquete.contenido, nodoActual.id, nodoActual.paquete.recorrido)
        }
    }
}