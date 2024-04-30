import Nodo from "../models/nodo.js"
import Grafo from "../models/grafo.js"

let colores = [
	'rgba(231, 76, 60, 0.8)',     // Rojo
	'rgba(142, 68, 173, 0.8)',    // Púrpura
	'rgba(52, 152, 219, 0.8)',    // Azul
	'rgba(46, 204, 113, 0.8)',    // Verde
	'rgba(243, 156, 18, 0.8)',    // Naranja
	'rgba(155, 89, 182, 0.8)',    // Violeta
	'rgba(26, 188, 156, 0.8)',    // Turquesa
	'rgba(241, 196, 15, 0.8)',    // Amarillo
	'rgba(189, 195, 199, 0.8)'    // Plata
  ]

export function dibujaGrafo(canvas, grafo) {

	let ancho = canvas.width,
		alto = canvas.height,
		radionodo = 20

	canvas = canvas.getContext("2d")

	let vertices_poligono = function (inicial_x, inicial_y, num_vertices, longitud_arista) {
		let punto = { x: inicial_x, y: inicial_y },
			poligono = [],
			w = 2 * Math.PI / num_vertices

		poligono.push(punto)

		for (let i = 1; i < num_vertices; i++) {
			let x = parseInt(Math.cos(w * (i - 1)) * longitud_arista + poligono[i - 1].x)
			let y = parseInt(Math.sin(w * (i - 1)) * longitud_arista + poligono[i - 1].y)
			punto = { x: x, y: y }
			poligono.push(punto)
		}

		return poligono
	}

	let posicion_nodos = function (num_nodos) {
		let coordenadasNodos = {}
		let resultados = vertices_poligono(0, 0, num_nodos, ancho / (num_nodos / 2)),
			menor_x = 0,
			mayor_x = 0,
			menor_y = 0,
			mayor_y = 0,
			inicial_x = 0,
			inicial_y = 0

		radionodo = ancho / (num_nodos * 2.5)

		//Escogemos el menor
		for (let i = 1; i < num_nodos; i++) {
			if (resultados[i].x < menor_x) menor_x = -resultados[i].x
			if (resultados[i].x > mayor_x) mayor_x = resultados[i].x
			if (resultados[i].y < menor_y) menor_y = -resultados[i].y
			if (resultados[i].y > mayor_y) mayor_y = resultados[i].y
		}

		inicial_x = (menor_x + ancho - mayor_x) / 2
		inicial_y = (menor_y + ancho - mayor_y) / 2

		resultados = vertices_poligono(inicial_x, inicial_y, num_nodos, ancho / (num_nodos / 2))

		if (grafo instanceof Grafo) {
			for (let i = 0; i < grafo.nodos.length; i++) {
				coordenadasNodos[grafo.nodos[i].id] = resultados[i]
			}
		}
		return coordenadasNodos
	}

	let dibuja_nodo = function (centro, id) {
		let radio = radionodo
		canvas.beginPath()
		canvas.arc(centro.x, centro.y, radio, 0, 2 * Math.PI, false)
		canvas.lineWidth = 2
		
		if(grafo instanceof Grafo){
			canvas.strokeStyle = colores[grafo.obtenerNodo(id).color]
			canvas.fillStyle = colores[grafo.obtenerNodo(id).color]
		}
		canvas.stroke()
		canvas.fill()
		canvas.fillStyle = '#fff'
		canvas.font = parseInt(radio) + 'px Arial'
		canvas.fillText(id, centro.x - (radio / 3), centro.y + (radio / 3))
	}

	let dibuja_arista = function (origen, destino, id) {
		canvas.fillStyle = '#000000'
		let angulo = Math.atan2(destino.y - origen.y, destino.x - origen.x),
			origen_x = origen.x + radionodo * Math.cos(angulo),
			origen_y = origen.y + radionodo * Math.sin(angulo),
			destino_x = destino.x - radionodo * Math.cos(angulo),
			destino_y = destino.y - radionodo * Math.sin(angulo)
		canvas.beginPath()
		canvas.moveTo(origen_x, origen_y)
		canvas.lineTo(destino_x, destino_y)
		canvas.lineWidth = 2
		canvas.strokeStyle = "#000000"
		canvas.stroke()
		canvas.font = parseInt(radionodo / 1.5) + 'px Arial'
		canvas.fillText(id, (destino_x + origen_x) / 2, (destino_y + origen_y) / 2)
	}
	let num_nodos = 0
	if (grafo instanceof Grafo) {
		num_nodos = grafo.nodos.length
	}

	//console.log(`numero de nodos ${num_nodos}`)
	let vertices = posicion_nodos(num_nodos)

	//Borramos el dibujo anterior
	canvas.clearRect(0, 0, ancho, alto)
	if (grafo instanceof Grafo) {
		for (let nodo of grafo.nodos) {
			if (nodo instanceof Nodo) {
				//console.log(`coordenadas nodo ${nodo.id}: ${vertices[nodo.id].x}, ${vertices[nodo.id].y}`)
				dibuja_nodo(vertices[nodo.id], nodo.id)
				for (let vecinoId in nodo.vecinos) {
					dibuja_arista(vertices[nodo.id], vertices[vecinoId], nodo.vecinos[vecinoId])
				}
			}
		}
	}
	return canvas
}
