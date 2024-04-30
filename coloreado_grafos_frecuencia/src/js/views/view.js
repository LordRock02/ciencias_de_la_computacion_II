export default class View {
    constructor() {
        this.resultado = document.getElementById('resultado')
        this.cantidad = document.getElementById('cantidad')
        this.aumentarBtn = document.getElementById('aumentar')
        this.disminuirBtn = document.getElementById('disminuir')
        this.canvasGrafo = document.getElementById('grafo')
        this.tabla = document.getElementById('tabla')
    }
    bindAumentarBtn(handler){
        this.aumentarBtn.addEventListener('click', handler)
    }
    bindDisminuirBtn(handler){
        this.disminuirBtn.addEventListener('click', handler)
    }    
    updateTable(head, body) {
        this.tabla.innerHTML = ``
        this.tabla.appendChild(head)
        this.tabla.appendChild(body)
    }
}