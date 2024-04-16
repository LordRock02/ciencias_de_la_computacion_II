export default class View {
    constructor() {
        this.inputMessage = document.getElementById('inputMessage')
        this.sendBtn = document.getElementById('send')
        this.table = document.getElementById('table')
        this.canvasGrafo = document.getElementById('grafo')
        this.clearBtn = document.getElementById('clear')
        this.selectOrigen = document.getElementById('origen')
        this.selectDestino = document.getElementById('destino')
    }

    bindSendMessage(handler) {
        this.sendBtn.addEventListener('click', handler)
    }

    bindClearTable(handler){
        this.clearBtn.addEventListener('click', handler)
    }

    updateTable(row) {
        this.table.appendChild(row)
    }
}   