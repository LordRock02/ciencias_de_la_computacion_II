const opcionOrigen = document.getElementById('opcionOrigen')
const opcionDestino = document.getElementById('opcionDestino')
const opcionAlgoritmo = document.getElementById('opcionAlgoritmo')
const divResultado = document.getElementById('resultado')
const nodosInicialesEndPoint = `/get-coordenadas`

const cargarNodos = async (ENDPOINT) => {
  try {
    const response = await fetch(ENDPOINT, { method: 'POST' });
    const data = await response.json();
    console.log(ENDPOINT)
    console.log(data)
    return data;
  } catch (error) {
    console.error('Error al cargar las coordenadas:', error);
    return null;
  }
};


const map = L.map('map').setView([4.6482783,-74.2729636], 5);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

const limpiarMapa = (map) => {
  map.eachLayer((layer) => {
      if (layer instanceof L.Layer && !(layer instanceof L.TileLayer)) {
          map.removeLayer(layer);
      }
  })
}

const setMarcadores = (map, nodos) => {
  if (nodos) {
    for (let dep in nodos) {
      if (nodos.hasOwnProperty(dep)) {
        let coordenadas = nodos[dep];
        L.marker([coordenadas.latitud, coordenadas.longitud]).addTo(map);
      }
    }
  }
}

const dibujarAristas = (map, nodos, parameters = null) => {
  if(nodos){
    for (let dep in nodos) {
      if (nodos.hasOwnProperty(dep)) {
        let coordenadas = nodos[dep];
        for (let vecino in coordenadas.vecinos) {
          if (coordenadas.vecinos.hasOwnProperty(vecino)) {
            let coordenadasV = coordenadas.vecinos[vecino];
            if(!parameters){
              var polyline = L.polyline([[coordenadas.latitud, coordenadas.longitud], [coordenadasV.latitud, coordenadasV.longitud]], {color:'green'}).addTo(map);
            }else{
              var polyline = L.polyline([[coordenadas.latitud, coordenadas.longitud], [coordenadasV.latitud, coordenadasV.longitud]], parameters).addTo(map);
            }
          }
        }
      }
    }
  }
}

const dibujarGrafoInicial = async (map) => {
  let nodos = await cargarNodos(nodosInicialesEndPoint)
  setMarcadores(map, nodos)
  dibujarAristas(map, nodos)
}

const dibujarSpanningTree = async (map, ENDPOINT) => {
  let nodos = await cargarNodos(ENDPOINT)
  dibujarAristas(map, nodos, parameters={color:'rgba(0, 0, 255, 0.3)', weight: 15})
}

const dibujarRuta = (map, arr) => {
  //setMarcadores(map)
    arr.forEach(segmento => {
      console.log(`${segmento.a}, ${segmento.b}`)
      var polyline = L.polyline([segmento.a, segmento.b], {color:'rgba(255, 0, 0, 0.5)', weight: 10}).addTo(map)
    });
    //var polyline = L.polyline([[6.244197, -75.6637852], [5.454516, -73.362031]], {color:'red'}).addTo(map)
}

const setResultado = (distancia, ruta) => {
  divResultado.innerHTML = `<div><h1>distancia : ${distancia}</h1></div><div><h1>ruta: ${ruta}</h1></div>`
}


dibujarGrafoInicial(map)


const calcular = () => { 
  limpiarMapa(map)
  dibujarGrafoInicial(map)
  const origen = opcionOrigen.value
  const destino = opcionDestino.value
  const algoritmo = opcionAlgoritmo.value
  console.log(`origen: ${origen} destino: ${destino}`)
  if (algoritmo == 'Dijkstra' || algoritmo == 'A*'){
    fetch(`/calcular-ruta/${origen}/${destino}/${algoritmo}`, {method: 'POST'})
    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(`distancia: ${data.distancia} ruta: ${data.ruta}`)
      console.log(`segmentos ruta: ${data.segmentosRuta}`)
      data.segmentosRuta.forEach(segmento => {
        console.log(`${segmento.a}, ${segmento.b}`)
      })
      dibujarRuta(map, data.segmentosRuta)
      setResultado(data.distancia, data.ruta)
    })
  }else{
    const origen = opcionOrigen.value
    if(algoritmo == 'Kruskal'){
      dibujarSpanningTree(map, `/spanning-tree/${algoritmo}/${null}`)
    }else{
      dibujarSpanningTree(map, `/spanning-tree/${algoritmo}/${origen}`)
    }
    
  }
}