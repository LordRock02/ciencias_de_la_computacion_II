export default class View {
    constructor() {
        this.inputMessage = document.getElementById('inputMessage')
        this.sendBtn = document.getElementById('send')
        this.table = document.getElementById('table')
        this.canvasGrafo = document.getElementById('grafo')
    }

    bindSendMessage(handler) {
        this.sendBtn.addEventListener('click', handler)
    }

    updateTable(row) {
        this.table.appendChild(row)
    }
}   