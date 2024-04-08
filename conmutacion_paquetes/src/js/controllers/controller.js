import Grafo from "../models/grafo.js";
import View from "../views/view.js";

export default class Controller {
    constructor(grafo, view) {
        if (grafo instanceof Grafo) {
            this.grafo = grafo
        }
        if (view instanceof View) {
            this.view = view
        }

        this.view.bindSendMessage(this.handleTable.bind(this))

    }
    handleTable() {
        this.render()
    }
    render() {
        let newRow = document.createElement('tr')
        newRow.innerHTML = `
        <th scope='row'>1</th>
        <td>${this.view.inputMessage.value}</td>
        <td>1</td>`
        this.view.updateTable(newRow)
    }
}