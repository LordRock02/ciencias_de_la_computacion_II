const opcionOrigen = document.getElementById('opcionOrigen')
const opcionDestino = document.getElementById('opcionDestino')

let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");

  map = new Map(document.getElementById("map"), {
    center: { lat: 10.759581, lng: -74.776339 },
    zoom: 8,
  });
}


const calcular = () => { 
  const origen = opcionOrigen.value
  const destino = opcionDestino.value
  console.log(`origen: ${origen} destino: ${destino}`)
  fetch(`/calcular-ruta/${origen}/${destino}`, {method: 'POST'})
    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(`resultado: ${data}`)
      console.log('Resultado Dijkstra:', data.dijkstra)
      console.log('Resultado A*:', data['A*'])
    })
}