import Grafo from "../models/grafo";
import View from "../views/view";
import Nodo from "../models/nodo";
import { dibujaGrafo } from "./dibujaGrafo";

const tableHead = (nodos) => {
    let head = document.createElement('thead')
    let row = document.createElement('tr')
    row.innerHTML += `<th/>`
    if (nodos instanceof Array) {
        nodos.forEach(nodo => row.innerHTML += `<th>${nodo}</th>`)
    }
    head.appendChild(row)
    console.log(head.innerHTML)
    return(head)
}

const tableBody = (nodos) => {
    let body = document.createElement('tbody')
    const aristasVisitadas = []
    nodos.forEach(nodo=>{
        if(nodo instanceof Nodo){
            let row = document.createElement('tr')
            row.innerHTML += `<td>${nodo.id}</td>`
            for (let i = 1; i <= nodo.grado + 1; i++){
                if(nodo.vecinos[i] != undefined && !aristasVisitadas.some(arr => arr[0] === i && arr[1] === nodo.id)){
                    row.innerHTML += `<td><input id='${nodo.id}-${i}' value=${nodo.vecinos[i]} class='aristaInput'></td>`
                    aristasVisitadas.push([nodo.id, i])
                }else{
                    row.innerHTML += `<td/>`
                }
                
            }
            body.appendChild(row)
        }
    })
    console.log(body.innerHTML)
    return(body)
}

export default class Controller {
    constructor(grafo, view) {
        if (grafo instanceof Grafo) {
            this.grafo = grafo
        }
        if (view instanceof View) {
            this.view = view
        }
        this.renderGrafo()
        this.view.bindAumentarBtn(this.aumentarNodos.bind(this))
        this.view.bindDisminuirBtn(this.disminuirNodos.bind(this))
        this.view.bindAristaInputs(this.actualizarNodos.bind(this))
    }

    aumentarNodos() {
        const cantidad = parseInt(this.view.cantidad.innerText)
        this.view.cantidad.innerText = cantidad + 1
        this.grafo.crearNodo()
        this.renderGrafo()
    }
    disminuirNodos() {
        const cantidad = parseInt(this.view.cantidad.innerText)
        if (cantidad >= 1) {
            this.view.cantidad.innerText = cantidad - 1
            this.grafo.eliminarNodo(this.grafo.nodos[this.grafo.nodos.length - 1].id)
            this.renderGrafo()
        }
    }

    actualizarNodos(id, value){
        const nodos = id.split('-')
        this.grafo.setPesoArista(nodos[0], nodos[1], value)
        this.renderGrafo()
    }

    renderGrafo() {
        let numCromatico = this.grafo.coloreadoGrafo()
        this.view.canvasGrafo.getContext('2d').clearRect(0, 0, this.view.canvasGrafo.width, this.view.canvasGrafo.height)
        //this.grafo.actualizarAristas()
        dibujaGrafo(this.view.canvasGrafo, this.grafo)
        this.view.resultado.innerText = `numero cromatico: ${numCromatico}`
        this.view.updateTable(tableHead(this.grafo.listaIdNodos()), tableBody(this.grafo._nodos))
        //delete this.view
        this.view = new View()
        this.view.bindAristaInputs(this.actualizarNodos.bind(this))
    }
}