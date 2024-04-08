import Grafo from "../models/grafo.js";
import Nodo from "../models/nodo.js";
import { grafo_condorcet } from "../controllers/grafocondorcet.js";
import Controller from "../controllers/controller.js";
import View from "../views/view.js";


function dibuja(grafo = null) {
  var canvas = grafo_condorcet('grafo', grafo);
}


const nodos = [
  new Nodo(1),
  new Nodo(2),
  new Nodo(3),
  new Nodo(4),
  new Nodo(5),
  new Nodo(6),
  new Nodo(7),
  new Nodo(8),
  new Nodo(9)
]

const grafo = new Grafo(nodos)
const view = new View()

grafo.agregarVecinosNodo(1, { 5: 7, 3: 3, 2: 5 })
grafo.agregarVecinosNodo(2, { 3: 4, 4: 8 })
grafo.agregarVecinosNodo(3, { 4: 6, 5: 2, 6: 9 })
grafo.agregarVecinosNodo(4, { 8: 1 })
grafo.agregarVecinosNodo(5, { 6: 3, 7: 7 })
grafo.agregarVecinosNodo(6, { 7: 4, 8: 2, 9: 5 })
grafo.agregarVecinosNodo(9, { 8: 6, 7: 8 })

const controller = new Controller(grafo, view)

console.log(grafo)
dibuja(grafo)