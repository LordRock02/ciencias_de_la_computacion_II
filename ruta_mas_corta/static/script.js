const opcionOrigen = document.getElementById('opcionOrigen')
const opcionDestino = document.getElementById('opcionDestino')
const opcionAlgoritmo = document.getElementById('opcionAlgoritmo')
const divResultado = document.getElementById('resultado')

const cargarCoordenadas = async () => {
  try {
    const response = await fetch('/get-coordenadas', { method: 'POST' });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error al cargar las coordenadas:', error);
    return null;
  }
};


var map = L.map('map').setView([4.6482783,-74.2729636], 5);

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

const setMarcadores = async (map) => {
  let coordenadasIniciales = await cargarCoordenadas();
  if (coordenadasIniciales) {
    console.log('Coordenadas iniciales:', coordenadasIniciales);
    for (let dep in coordenadasIniciales) {
      if (coordenadasIniciales.hasOwnProperty(dep)) {
        let coordenadas = coordenadasIniciales[dep];
        console.log(`dep: ${dep} coordenadas: ${coordenadas.latitud}, ${coordenadas.longitud}`);
        L.marker([coordenadas.latitud, coordenadas.longitud]).addTo(map);
        for (let vecino in coordenadas.vecinos) {
          if (coordenadas.vecinos.hasOwnProperty(vecino)) {
            let coordenadasV = coordenadas.vecinos[vecino];
            var polyline = L.polyline([[coordenadas.latitud, coordenadas.longitud], [coordenadasV.latitud, coordenadasV.longitud]], {color:'green'}).addTo(map);
          }
        }
      }
    }
  } else {
    console.log('No se pudieron cargar las coordenadas.');
    return {};
  }
}

const dibujarRuta = (map, arr) => {
  //setMarcadores(map)
    arr.forEach(segmento => {
      console.log(`${segmento.a}, ${segmento.b}`)
      var polyline = L.polyline([segmento.a, segmento.b], {color:'red'}).addTo(map)
    });
    //var polyline = L.polyline([[6.244197, -75.6637852], [5.454516, -73.362031]], {color:'red'}).addTo(map)
}

const setResultado = (distancia, ruta) => {
  divResultado.innerHTML = `<div><h1>distancia : ${distancia}</h1></div><div><h1>ruta: ${ruta}</h1></div>`
}


setMarcadores(map);


const calcular = () => { 
  limpiarMapa(map)
  setMarcadores(map)
  const origen = opcionOrigen.value
  const destino = opcionDestino.value
  const algoritmo = opcionAlgoritmo.value
  console.log(`origen: ${origen} destino: ${destino}`)
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
}