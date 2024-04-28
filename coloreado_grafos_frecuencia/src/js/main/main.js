import Grafo from "../models/grafo";
import Nodo from "../models/nodo";
import { dibujaGrafo } from "../controllers/dibujaGrafo";

const nodos = [
  new Nodo(1),
  new Nodo(2),
  new Nodo(3),
  new Nodo(4),
  new Nodo(5),
  new Nodo(6)
]

const grafo = new Grafo(nodos)
grafo.agregarVecinosNodo(1, { 2: 85, 3: 175, 4: 200, 5: 50, 6: 100 })
grafo.agregarVecinosNodo(2, { 3: 125, 4: 175, 5: 100, 6: 160 })
grafo.agregarVecinosNodo(3, { 4: 100, 5: 200, 6: 250 })
grafo.agregarVecinosNodo(4, { 5: 210, 6: 220 })
grafo.agregarVecinosNodo(5, { 6: 100 })


console.log(`cantidad de colores necesarios: ${grafo.coloreadoGrafo()}`)
console.log(grafo)
dibujaGrafo(document.getElementById('grafo'), grafo)
document.getElementById('resultado').innerText = `numero de colores necesarios: ${grafo.coloreadoGrafo()}`