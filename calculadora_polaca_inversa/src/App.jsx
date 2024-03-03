/* eslint-disable no-unused-vars */
import { useState } from 'react'
import './App.css'
import { evaluate } from '.'
import { Node } from './BinaryTree'
import { BinaryTree } from './BinaryTree'


function App() {
  const display = document.getElementById('display')
  console.log('inicio el programa')
  let arr = ('4 3 ↑ 6 2 ↑ + 4 5 * + 3 2 ↑ 8 2 / - /'.split(' ')).reverse()
  const appendToDisplay = (input) => {
    const display = document.getElementById('display')
    const value = display.getAttribute('value') != null? display.getAttribute('value'):''
    display.setAttribute('value', value + input)
  }
  const clearDisplay = () => {
    const display = document.getElementById('display')
    display.setAttribute('value', '')
  }
  const erase = () => {
    const display = document.getElementById('display')
    let value = display.getAttribute('value') != null? display.getAttribute('value'):''
    value = value.slice(0,-1)
    display.setAttribute('value', value)
  }
  const setResult = () => {
    const display = document.getElementById('display')
     let res = evaluate(display.getAttribute('value'))
     display.setAttribute('value', res)
  }
  const createNode = (node, child1, child2) => {
    return(<Node node={node} child1={child1} child2={child2}></Node>)
  }
  return (
    <>
      <section id='calculadora'>
        <div id='calculator'>
          <input id='display' readOnly/>
          <div id='keys'>
            <button className='operator-btn' onClick={() => appendToDisplay('+')}>+</button>
            <button onClick={() => appendToDisplay('7')}>7</button>
            <button onClick={() => appendToDisplay('8')}>8</button>
            <button onClick={() => appendToDisplay('9')}>9</button>
            <button className='operator-btn' onClick={() => appendToDisplay('-')}>-</button>
            <button onClick={() => appendToDisplay('4')}>4</button>
            <button onClick={() => appendToDisplay('5')}>5</button>
            <button onClick={() => appendToDisplay('6')}>6</button>
            <button className='operator-btn' onClick={() => appendToDisplay('*')}>*</button>
            <button onClick={() => appendToDisplay('1')}>1</button>
            <button onClick={() => appendToDisplay('2')}>2</button>
            <button onClick={() => appendToDisplay('3')}>3</button>
            <button className='operator-btn' onClick={() => appendToDisplay('/')}>/</button>
            <button onClick={() => appendToDisplay('0')}>0</button>
            <button onClick={() => appendToDisplay('.')}>.</button>
            <button className='operator-btn' onClick={() => {setResult()}}>=</button>
            <button className='operator-btn' onClick={() => appendToDisplay('↑')}>↑</button>
            <button className='operator-btn' onClick={() => appendToDisplay(' ')}>_</button>
            <button className='operator-btn' onClick={() => erase()}>←</button>
            <button className='operator-btn' onClick={() => clearDisplay()}>C</button>
          </div>
        </div>      
      </section>
      <section className='full-height'>
        <div id='binary-tree'>
          <BinaryTree stack={arr}></BinaryTree>
        </div>
      </section>
    </>
  )
}

export default App
