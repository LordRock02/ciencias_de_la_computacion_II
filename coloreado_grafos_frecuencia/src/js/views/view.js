export default class View {
    constructor() {
        this.resultado = document.getElementById('resultado')
        this.cantidad = document.getElementById('cantidad')
        this.aumentarBtn = document.getElementById('aumentar')
        this.disminuirBtn = document.getElementById('disminuir')
        this.canvasGrafo = document.getElementById('grafo')
        this.tabla = document.getElementById('tabla')
        this.aristaInputs = document.querySelectorAll('.aristaInput')
    }
    bindAumentarBtn(handler) {
        this.aumentarBtn.addEventListener('click', handler)
    }
    bindDisminuirBtn(handler) {
        this.disminuirBtn.addEventListener('click', handler)
    }
    bindAristaInputs(handler) {
        const agregarEventListener = (input) => {
            input.addEventListener('change', () => {
              handler(input.id, input.value)
            })
          }
        
          this.aristaInputs = document.querySelectorAll('.aristaInput');
          this.aristaInputs.forEach(agregarEventListener)
        
        //   document.addEventListener('change', (event) => {
        //     if (event.target && event.target.classList.contains('aristaInput')) {
        //       agregarEventListener(event.target)
        //     }
        //   })
    }
    updateTable(head, body) {
        this.tabla.innerHTML = ``
        this.tabla.appendChild(head)
        this.tabla.appendChild(body)
    }
}